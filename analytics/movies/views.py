from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .services import MovieService
from .forms import SearchMovie, YearFilter

service = MovieService()


class HomeView(View):
    def get(self, request):
        movies = service.get_movies()
        genres = service.get_genres()
        context = {
            'total_movies': len(movies),
            'total_genres': len(genres['labels'])
        }
        return render(request, 'pages/index.html', context)


class MovieView(View):
    def get(self, request, title):
        movie = service.get_movie(title)
        if movie is None:
            return redirect('/error/not-found')
        return render(request, 'pages/movie.html', {'movie': movie})


class RatingsChartView(View):
    def get(self, request):
        sorted = request.GET.get('sorted', '')
        chart_data = service.get_top_rated() if sorted == 'True' else service.get_imdb_ratings()
        return JsonResponse(chart_data)


class MonthsChartView(View):
    def get(self, request):
        form = YearFilter(request.GET)
        if form.is_valid():
            year = form.cleaned_data['year']
        else:
            year = ''
        chart_data = service.months_data(year)
        return JsonResponse(chart_data)


class GenresChartView(View):
    def get(self, request):
        chart_data = service.get_genres()
        return JsonResponse(chart_data)


class AvgRatingsView(View):
    def get(self, request):
        chart_data = service.genres_avg_ratings()
        return JsonResponse(chart_data)


def get_movies(request):
    form = SearchMovie(request.GET)
    if (form.is_valid()):
        title = form.cleaned_data['title']
        filter = {'title': title}
    else:
        filter = {}
    movies = service.get_movies(filter)
    return JsonResponse({'movies': movies})

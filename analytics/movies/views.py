from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .services import MovieService
from .forms import SearchMovie

service = MovieService()


class GenresView(View):
    def get(self, request):
        return render(request, 'pages/genres.html')


class MoviesView(View):
    def get(self, request):
        return render(request, 'pages/movies.html')


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


class GenresChartView(View):
    def get(self, request):
        chart_data = service.get_genres_data()
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

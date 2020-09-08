from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .repository import MovieRepo
from .forms import SearchMovie
import numpy as np


def index(response):
    form = SearchMovie()
    return render(response, 'pages/index.html', {'form': form})


def get_movies(request):
    form = SearchMovie(request.GET)
    if (form.is_valid()):
        title = form.cleaned_data['title']
        movies = MovieRepo.get_movies({'title': title})

    else:
        movies = MovieRepo.get_movies()

    response = {'movies': movies}

    return JsonResponse(response)


def get_movie(request):
    movie = MovieRepo.get_movie('Legend')
    response = {
        'movie': movie
    }

    return JsonResponse(response)


def imdb_ratings(request):
    movies = MovieRepo.get_movies()
    titles = map(lambda movie: movie['title'], movies)
    ratings = map(lambda movie: movie['imdbRating'], movies)

    dataset = {
        'labels': list(titles),
        'data': list(ratings)
    }

    return JsonResponse(dataset)


def genres_data(request):
    genres = MovieRepo.get_genres()
    data = np.arange(len(genres))
    data.fill(0)

    for i in range(len(genres)):
        movies = MovieRepo.get_movies({'genre': genres[i]})
        data[i] = len(movies)

    dataset = {
        'genres': genres,
        'count': data.tolist()
    }

    return JsonResponse(dataset)

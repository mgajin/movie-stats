from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .repository import MovieRepo


def get_movies(request):
    movies = MovieRepo.get_all()
    response = {
        'movies': movies
    }

    return JsonResponse(response)


def get_movie(request):
    movie = MovieRepo.get_movie('Legend')
    response = {
        'movie': movie
    }

    return JsonResponse(response)

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import MovieModel


def get_movies(request):

    data = MovieModel.get_all()

    for movie in data:
        print(movie)

    return JsonResponse({})

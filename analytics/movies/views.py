from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .repository import MovieRepo


def get_movies(request):

    data = MovieRepo.get_all()

    for movie in data:
        print(movie)

    context = {
        'success': True
    }

    return JsonResponse(context)

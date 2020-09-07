from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_movies),
    path('imdb', views.imdb_ratings),
    path('genres', views.genres_data)
]

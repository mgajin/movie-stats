from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('movies/', views.get_movies),
    # path('movies/<int:title>', views.get_movie),
    path('imdb', views.imdb_ratings),
    path('genres', views.genres_data)
]

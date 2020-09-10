from django.contrib import admin
from django.urls import path
from .views import HomeView, MoviesView, GenresView, GenresChartView, RatingsChartView, get_movies

urlpatterns = [
    path('', HomeView.as_view()),
    path('movies/', MoviesView.as_view()),
    # path('movies/<int:title>', views.MovieView.as_view()),
    path('genres/', GenresView.as_view()),
    path('charts/imdb', RatingsChartView.as_view()),
    path('charts/genres', GenresChartView.as_view()),
    path('api/movies', get_movies)
]

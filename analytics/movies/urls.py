from django.contrib import admin
from django.urls import path
from .views import HomeView, MovieView, GenresChartView, RatingsChartView, get_movies

urlpatterns = [
    path('', HomeView.as_view()),
    path('movies/<str:title>', MovieView.as_view()),
    path('charts/imdb', RatingsChartView.as_view()),
    path('charts/genres', GenresChartView.as_view()),
    path('api/data', get_movies)
]

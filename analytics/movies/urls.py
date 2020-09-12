from django.contrib import admin
from django.urls import path
from .views import HomeView, MovieView, MonthsChartView, GenresChartView, RatingsChartView, get_movies

urlpatterns = [
    path('', HomeView.as_view()),
    path('movies/<str:title>', MovieView.as_view()),
    path('charts/imdb', RatingsChartView.as_view()),
    path('charts/genres', GenresChartView.as_view()),
    path('charts/months', MonthsChartView.as_view()),
    path('api/movies', get_movies)
]

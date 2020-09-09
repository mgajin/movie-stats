from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('movies/', views.MoviesView.as_view()),
    path('genres/', views.GenresView.as_view()),
    # path('movies/<int:title>', views.get_movie),
    path('charts/imdb', views.imdb_ratings),
    path('charts/genres', views.genres_data)
]

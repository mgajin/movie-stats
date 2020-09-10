from django.http import JsonResponse
from .repository import MovieRepo
import numpy as np


class MovieService():
    def __init__(self):
        self.repository = MovieRepo()

    def get_ratings_data(self):
        movies = self.repository.get_movies()
        titles = map(lambda movie: movie['title'], movies)
        ratings = map(lambda movie: movie['imdbRating'], movies)

        dataset = {
            'labels': list(titles),
            'data': list(ratings)
        }

        return dataset

    def get_genres_data(self):
        genres = self.repository.get_genres()
        data = np.arange(len(genres))
        data.fill(0)

        for i in range(len(genres)):
            movies = self.get_movies({'genre': genres[i]})
            data[i] = len(movies)

        dataset = {
            'labels': genres,
            'data': data.tolist()
        }

        return dataset

    def get_movies(self, filter={}):
        return self.repository.get_movies(filter)

    def get_movie(self, title):
        return self.repository.get_movie(title)

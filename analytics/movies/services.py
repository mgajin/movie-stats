from django.http import JsonResponse
from .repository import MovieRepo
import numpy as np


class MovieService():
    def __init__(self):
        self.repository = MovieRepo()

    def get_imdb_ratings(self):
        movies = self.repository.get_movies()
        return self.__get_dataset(movies, 'title', 'imdbRating')

    def get_top_rated(self, n=10):
        movies = self.repository.get_movies_sorted()
        return self.__get_dataset(movies[:n], 'title', 'imdbRating')

    def get_genres(self):
        genres = self.repository.get_genres()
        data = np.arange(len(genres))
        data.fill(0)
        for i in range(len(genres)):
            movies = self.repository.get_movies({'genre': genres[i]})
            data[i] = len(movies)
        return {'labels': genres, 'data': data.tolist()}

    def get_movies(self, filter={}):
        return self.repository.get_movies(filter)

    def get_movie(self, title):
        return self.repository.get_movie(title)

    def __get_dataset(self, items, col_1, col_2):
        labels = map(lambda item: item[col_1], items)
        data = map(lambda item: item[col_2], items)
        return {'labels': list(labels), 'data': list(data)}

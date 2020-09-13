from django.http import JsonResponse
from .repository import MovieRepo
import numpy as np
import calendar


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
        return self.__response(genres, data.tolist())

    def genres_avg_ratings(self):
        genres = self.repository.get_genres()
        data = np.arange(len(genres), dtype='f')
        data.fill(0)
        for i in range(len(genres)):
            movies = self.repository.get_movies({'genre': genres[i]})
            avg = self.__get_average(movies, 'imdbRating')
            data[i] = avg
        return self.__response(genres, data.tolist())

    def months_data(self, year=''):
        months = calendar.month_name[1:]
        data = np.arange(len(months))
        data.fill(0)
        for i in range(len(months)):
            movies = self.repository.by_released_date(months[i][:3], year)
            data[i] = len(movies)
        return self.__response(months, data.tolist())

    def years_data(self):
        years = np.arange(2010, 2020)
        data = np.arange(len(years))
        data.fill(0)
        for i in range(len(years)):
            movies = self.repository.by_year(years[i])
            data[i] = len(movies)
        return self.__response(years.tolist(), data.tolist())

    def get_movies(self, filter={}):
        return self.repository.get_movies(filter)

    def get_movie(self, title):
        return self.repository.get_movie(title)

    def __get_average(self, items, col):
        avg = 0
        for item in items:
            avg += item[col]
        avg = float(avg) / len(items)
        return round(avg, 2)

    def __get_dataset(self, items, col_1, col_2):
        labels = map(lambda item: item[col_1], items)
        data = map(lambda item: item[col_2], items)
        return self.__response(list(labels), list(data))

    def __response(self, labels, data):
        return {'labels': labels, 'data': data}

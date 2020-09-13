from . import MovieCollection
from .models import Movie


class MovieRepo():
    def __init__(self):
        self.collection = MovieCollection.collection
        self.genres = MovieCollection.genres

    def get_movies(self, filter={}):
        data = self.collection.find(filter)
        movies = map(Movie.map_movie, data)
        return list(movies)

    def get_movies_sorted(self, filter={}):
        movies = self.get_movies(filter)
        return sorted(movies, key=self.__imdb_rating, reverse=True)

    def by_released_date(self, month, year):
        movies = self.get_movies()
        filtered = self.__filter_by_date(movies, month, year)
        return list(filtered)

    def by_year(self, year):
        movies = self.get_movies()
        filtered = filter(lambda movie: self.__year(movie, year), movies)
        return list(filtered)

    def get_movie(self, title):
        data = self.collection.find_one({'title': title})
        return data if data is None else Movie.map_movie(data)

    def get_genres(self):
        return self.genres

    def __filter_by_date(self, movies, month, year):
        return filter(lambda movie: self.__released(movie, month, year), movies)

    def __released(self, movie, month, year):
        return month in movie['released'] and year in movie['released']

    def __year(self, movie, year):
        return str(year) in movie['released']

    def __imdb_rating(self, movie):
        return movie['imdbRating']

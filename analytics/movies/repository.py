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

    def get_movie(self, title):
        data = self.collection.find_one({'title': title})
        return data if data is None else Movie.map_movie(data)

    def get_genres(self):
        return self.genres

    def __imdb_rating(self, movie):
        return movie['imdbRating']

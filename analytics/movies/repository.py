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
        return sorted(movies, key=lambda movie: movie['imdbRating'], reverse=True)

    def get_movie(self, title):
        data = self.collection.find_one({'title': title})
        if data is None:
            return data

        movie = Movie.map_movie(data)
        return movie

    def get_genres(self):
        return self.genres

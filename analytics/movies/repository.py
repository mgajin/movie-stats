from . import MovieCollection
from .models import Movie


class MovieRepo():
    collection = MovieCollection.collection

    @staticmethod
    def get_movies(filter={}):
        data = MovieRepo.collection.find(filter)
        movies = map(Movie.map_movie, data)

        return list(movies)

    @staticmethod
    def get_movie(title):
        data = MovieRepo.collection.find_one({'title': title})
        movie = Movie.map_movie(data)

        return movie

    @staticmethod
    def get_genres():
        return MovieCollection.genres

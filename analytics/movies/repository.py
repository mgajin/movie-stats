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

    def get_movie(self, title):
        data = self.collection.find_one({'title': title})
        print(data)
        movie = Movie.map_movie(data)

        return movie

    def get_genres(self):
        return self.genres

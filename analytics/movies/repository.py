from . import MovieCollection
from .models import Movie


class MovieRepo():
    collection = MovieCollection.collection

    @staticmethod
    def get_imdb_data():
        movies = MovieRepo.get_all()
        titles = map(lambda movie: movie['title'], movies)
        ratings = map(lambda movie: movie['imdbRating'], movies)

        return {
            'labels': list(titles),
            'data': list(ratings)
        }

    @staticmethod
    def get_all():
        data = MovieRepo.collection.find({})
        movies = map(Movie.map_movie, data)

        return list(movies)

    @staticmethod
    def get_movie(title):
        data = MovieRepo.collection.find_one({'title': title})
        movie = Movie.map_movie(data)

        return movie

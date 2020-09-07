from . import MovieCollection


class MovieModel():
    collection = MovieCollection.collection

    @staticmethod
    def get_all():
        return MovieModel.collection.find({})

    @staticmethod
    def get_movie(title):
        return MovieModel.collection.find_one({'title': title})

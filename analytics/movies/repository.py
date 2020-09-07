from . import MovieCollection


class MovieRepo():
    collection = MovieCollection.collection

    @staticmethod
    def get_all():
        return MovieRepo.collection.find({})

    @staticmethod
    def get_movie(title):
        return MovieRepo.collection.find_one({'title': title})

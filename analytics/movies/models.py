class Movie():

    @staticmethod
    def map_movie(movie):
        return {
            'title': movie['title'],
            'rating': movie['rating'],
            'imdbRating': movie['imdbRating'],
            'genre': movie['genre'],
            'released': movie['released']
        }

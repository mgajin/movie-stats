from analytics import Database


class MovieCollection():
    collection = Database.get_collection('movies')
    genres = [
        'Action',
        'Adventure',
        'Sci-Fi',
        'Comedy',
        'Drama',
        'Thriller',
        'Mystery',
        'Western',
        'Crime',
        'Fantasy'
    ]

from analytics import Database


class MovieCollection():
    collection = Database.get_collection('movies')
    genres = [
        'Action',
        'Adventure',
        'Asci-Fi',
        'Comedy',
        'Drama',
        'Thriller',
        'Mystery',
        'Western',
        'Crime',
        'Fantasy'
    ]

from pymongo import MongoClient
from django.conf import settings


class Database(MongoClient):
    host = settings.DATABASES['default']['CLIENT']['host']
    cluster = MongoClient(host)
    database = cluster['MovieDb']

    @staticmethod
    def get_collection(name):
        return Database.database[name]

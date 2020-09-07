from . import UserCollection
from .models import User


class UserRepo():
    collection = UserCollection.collection

    @staticmethod
    def get_all():
        data = UserRepo.collection.find({})
        users = map(User.map_user, data)

        return list(users)

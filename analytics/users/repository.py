from . import UserCollection


class UserRepo():
    collection = UserCollection.collection

    @staticmethod
    def get_all():
        return UserRepo.collection.find({})

from ..models.UserModel import UserModel


class UserFactory:
    """
    Creates a User object with the response from the user service
    """
    @staticmethod
    def create(response):
        return UserModel(response.json())
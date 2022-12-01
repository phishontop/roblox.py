from ..models.UserModel import UserModel
from ..models.ErrorModel import InvalidUser, RateLimit


class UserFactory:
    """
    Creates a User object with the response from the user service
    """
    @staticmethod
    def create(response):
        if response.status_code == 404:
            raise InvalidUser("User ID is invalid")
        
        elif response.status_code == 429:
            raise RateLimit("users.roblox.com has ratelimited requests")

        return UserModel(response.json())
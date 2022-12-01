from ..models.GroupModel import GroupModel
from ..models.ErrorModel import InvalidGroup, RateLimit


class GroupFactory:
    
    @staticmethod
    def create(response):
        if response.status_code == 400:
            raise InvalidGroup("Group ID is invalid")
        
        elif response.status_code == 429:
            raise RateLimit("group.roblox.com has ratelimited requests")

        return GroupModel(response.json())
    
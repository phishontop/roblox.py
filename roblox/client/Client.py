from ..services import UserService
from ..services import GroupService

class Client:
    
    def __init__(self) -> None:
        pass
        
    def fetch_user(self, roblox_id: int):
        return UserService.fetch_user(roblox_id=roblox_id)
    
    def fetch_group(self, group_id: int):
        return GroupService.fetch_group(group_id=group_id)
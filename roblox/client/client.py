from ..services import UserService


class Client:
    
    def __init__(self) -> None:
        print(f"Client object has been created")
        
    def fetch_user(self, roblox_id: int):
        print(f"Client fetching {roblox_id}")
        return UserService.fetch_user(roblox_id=roblox_id)
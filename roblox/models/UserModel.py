from ..managers.UserManager import UserManager

class UserModel(UserManager):

    def __init__(self, data: dict) -> None:
        super().__init__(roblox_id=data["id"])
        self.name = data["name"]
        self.display_name = data["displayName"]
        self.id = data["id"]
        self.description = data["description"]
        self.created = data["created"]
        
        
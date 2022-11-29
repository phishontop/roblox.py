

class UserModel:

    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.display_name = data["displayName"]
        self.id = data["id"]
        self.description = data["description"]
        self.created = data["created"]
        
        


class GroupModel:

    def __init__(self, data: dict) -> None:
        #super().__init__(roblox_id=data["id"])
        self.name = data["name"]
        self.id = data["id"]
        self.description = data["description"]
        self.member_count = data["memberCount"]

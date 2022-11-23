from .utilities.http import HttpClient
from .user import User
from .auth import Auth
from typing import Type
import json


class Role:
    """Represents a role in a group"""

    def __init__(self, data: dict) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.rank = data["rank"]


class BaseGroup:

    def __init__(self, group_id: int, auth_client: Type[Auth]) -> None:
        self.group_id = group_id
        self.group_client = HttpClient("groups.roblox.com")
        self.auth_client = auth_client

    def get_role(self, role_name: str) -> Role:
        response = self.group_client.get(f"/v1/groups/{self.group_id}/roles")
        json_response = json.loads(response[0].decode())

        for role in json_response["roles"]:
            if role_name == role["name"]:
                return Role(role)

    def set_role(self, role: Type[Role], user: Type[User]) -> None:
        pass






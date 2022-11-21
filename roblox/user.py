from typing import Type
from .utilities.http import HttpClient
import json
import time


class BaseUser:

    def __init__(self, roblox_id: int) -> None:
        self.roblox_id = roblox_id
        self.friends_client = HttpClient("friends.roblox.com")

    def get_friend_count(self) -> dict:
        response = self.friends_client.get(f"/v1/users/{self.roblox_id}/friends/count")
        return json.loads(response[0].decode())["count"]

    def get_follower_count(self) -> dict:
        response = self.friends_client.get(f"/v1/users/{self.roblox_id}/followers/count")
        return json.loads(response[0].decode())["count"]

    def get_followers(self, limit: int, max_page: int = 1) -> list:
        followers = []
        cursor = ""
        for page in range(max_page):
            response = self.friends_client.get(f"/v1/users/{self.roblox_id}/followers?sortOrder=Desc&limit={limit}&cursor={cursor}")
            response_json = json.loads(response[0].decode())
            cursor = response_json["nextPageCursor"]

            for follower in response_json["data"]:
                followers.append(User(follower))

            if cursor is None:
                break

        return followers

class User(BaseUser):

    def __init__(self, data: dict) -> None:
        for name, value in data.items():
            setattr(self, name, value)

        super().__init__(roblox_id=data["id"])

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"


class EventUser:

    def __init__(self, user: Type[User]) -> None:
        self.roblox_id = user.id
        self.base = BaseUser(roblox_id=user.id)

    def on_follower(self):
        count = self.base.get_follower_count()
        while True:
            time.sleep(5)
            new_count = self.base.get_follower_count()
            if new_count > count:
                return self.base.get_followers(limit=10, max_page=1)[0]
            elif new_count < count:
                count = new_count
















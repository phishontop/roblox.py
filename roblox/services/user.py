from ..http import HttpService
from ..managers.UserFactory import UserFactory

class UserService:

    @staticmethod
    def fetch_user(roblox_id: int):
        print(f"Manager User: fetch_user({roblox_id})")
        http_client = HttpService().client
        response = http_client.send_request(method="GET", link=f"https://users.roblox.com/v1/users/{roblox_id}")
        return UserFactory.create(response)
        
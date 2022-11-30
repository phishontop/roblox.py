from ..http import HttpService


class UserManager:

    def __init__(self, roblox_id: int) -> None:
        self.roblox_id = roblox_id
        self.http_client = HttpService().client
        
    def get_follower_count(self):
        response = self.http_client.send_request(
            method="GET",
            link=f"https://friends.roblox.com/v1/users/{self.roblox_id}/followers/count"
        )
        
        return response.json()["count"]
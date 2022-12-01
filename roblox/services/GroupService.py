from ..http import HttpService
from ..managers.GroupFactory import GroupFactory


class GroupService:
    
    @staticmethod
    def fetch_group(group_id: int):
        http_client = HttpService().client
        response = http_client.send_request(method="GET", link=f"https://groups.roblox.com/v1/groups/{group_id}")
        return GroupFactory.create(response)

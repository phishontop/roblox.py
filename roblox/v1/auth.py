from .utilities.http import HttpClient
from .utilities.error import AuthError
import json

class Auth:

    def __init__(self, cookie: str) -> None:
        self.cookie = cookie
        self.HTTPUser = HttpClient("users.roblox.com")
        self.HTTPAuth = HttpClient("auth.roblox.com")
        self.HTTPPresence = HttpClient("presence.roblox.com")

    def get_token(self) -> str:
        response = self.HTTPAuth.post(
            resource="/v2/login",
            data={},
            headers={"Cookie": self.cookie}
        )
        try:
            return response[1].decode().split("x-csrf-token: ")[1].split("\r\n")[0]

        except IndexError:
            raise AuthError("Authorization has been denied; the cookie is invalid.")

    def get_authenticated_id(self) -> int:
        response = self.HTTPUser.get(
            resource="/v1/users/authenticated",
            headers={
                "Cookie": self.cookie,
                "X-CSRF-TOKEN": self.get_token()
            }
        )

        response_text = response[0].decode()
        return json.loads(response_text)["id"]

    def set_presence(self, presence: dict) -> dict:
        response = self.HTTPPresence.post(
            resource="/v1/presence/register-app-presence",
            data=presence,
            headers={
                "Cookie": self.cookie,
                "X-CSRF-TOKEN": self.get_token()
            }
        )

        return json.loads(response[0].decode())

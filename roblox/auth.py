from .utilities.http import HttpClient
from .utilities.error import AuthError
import json

class Auth:

    def __init__(self, headers):
        self.headers = headers
        self.HTTPUser = HttpClient("users.roblox.com")
        self.HTTPAuth = HttpClient("auth.roblox.com")

    def set_token(self):
        response = self.HTTPAuth.post(
            resource="/v2/login",
            data={},
            headers=self.headers
        )
        try:
            self.headers["X-CSRF-TOKEN"] = response[1].decode().split("x-csrf-token: ")[1].split("\r\n")[0]

        except IndexError:
            raise AuthError("Authorization has been denied; the cookie is invalid.")

    def get_authenticated_id(self):
        response = self.HTTPUser.get(
            resource="/v1/users/authenticated",
            headers=self.headers
        )

        response_text = response[0].decode()
        if "Authorization" in response_text:
            raise AuthError("Authorization has been denied; the cookie is invalid.")

        return json.loads(response_text)["id"]




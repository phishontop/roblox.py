import time
from threading import Thread

import json

from .utilities.http import HttpClient
from .auth import Auth
from .user import User


class Client:

    def __init__(self) -> None:
        self.events = []
        self.headers = {}
        self.requirements = {"on_ready": self.client_ready}
        self.running = False
        self.user = None

    def login(self, cookie: str) -> None:
        self.headers["Cookie"] = f".ROBLOSECURITY={cookie}"

        auth_client = Auth(self.headers)
        auth_client.set_token()
        roblox_id = auth_client.get_authenticated_id()
        
        self.user = self.fetch_user(roblox_id=roblox_id)
        self.headers = auth_client.headers
        
    def fetch_user(self, roblox_id: int) -> User:
        user_client = HttpClient("users.roblox.com")
        response = user_client.get(f"/v1/users/{roblox_id}")
        return User(json.loads(response[0].decode()))

    def run_event(self, event, requirement):
        event_thread = Thread(target=event)
        while True:
            requirement_value = requirement()
            event_thread.start()
            if requirement_value == "break":
                break

    def client_ready(self):
        while True:
            if self.running:
                return "break"

    def start(self):
        # Start events
        for event in self.events:
            requirement = self.requirements[event.__name__]
            event_thread = Thread(target=self.run_event, args=(event, requirement))
            event_thread.start()

        self.running = True
        while True:
            time.sleep(1)

    def event(self, target):
        if callable(target) and target.__name__ in self.requirements:
            self.events.append(target)
        else:
            raise Exception(f"Event {target.__name__} is not found.")

    def run(self, cookie: str) -> None:
        try:
            self.login(cookie)
            self.start()

        except KeyboardInterrupt:
            # Shutdown sockets.
            # Clean up
            pass

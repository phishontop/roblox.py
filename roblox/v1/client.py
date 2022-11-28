import time
import ssl
import json
from threading import Thread
from .utilities.http import HttpClient
from .auth import Auth
from .user import User, EventUser


class Client:

    def __init__(self) -> None:
        self.events = []
        self.cookie = None
        self.running = False
        self.user = None
        self.auth_client = None

    def login(self, cookie: str) -> None:
        self.cookie = f".ROBLOSECURITY={cookie}"

        self.auth_client = Auth(cookie=self.cookie)
        roblox_id = self.auth_client.get_authenticated_id()

        self.user = self.fetch_user(roblox_id=roblox_id)

    def fetch_user(self, roblox_id: int) -> User:
        user_client = HttpClient("users.roblox.com")
        response = user_client.get(f"/v1/users/{roblox_id}")
        return User(json.loads(response[0].decode()))

    def run_event(self, event, requirement) -> None:
        while True:
            requirement_value = requirement()
            if requirement_value == "break":
                Thread(target=event).start()
                break

            else:
                Thread(target=event, args=(requirement_value,)).start()

    def client_ready(self) -> str:
        while True:
            if self.running:
                return "break"
            time.sleep(0.01)

    def set_activity(self, location: str) -> None:
        try:
            self.auth_client.set_presence({"location": location})
        except ssl.SSLEOFError:
            self.auth_client = Auth(cookie=self.cookie)
            self.auth_client.set_presence({"location": location})


    def start(self) -> None:
        # Define requirements needed to trigger the events.

        event_requirements = {
            "on_ready": self.client_ready,
            "on_follower": EventUser(self.user).on_follower
        }

        # Start events.
        threads = []
        for event in self.events:
            requirement = event_requirements[event.__name__]
            event_thread = Thread(target=self.run_event, args=(event, requirement))
            threads.append(event_thread)

        for thread in threads:
            thread.daemon = True
            thread.start()

        self.running = True
        while True:
            self.set_activity(location="Profile")
            time.sleep(60)

    def event(self, target) -> None:
        if callable(target):
            self.events.append(target)
        else:
            raise Exception(f"Event is not callable")

    def run(self, cookie: str) -> None:
        try:
            self.login(cookie)
            self.start()

        except KeyboardInterrupt:
            # Shutdown sockets.
            # Clean up
            pass

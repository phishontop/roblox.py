from .utilities.http import HttpClient
import json

class User:

    def __init__(self, data: dict) -> None:
        self.id = data["id"]


    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"






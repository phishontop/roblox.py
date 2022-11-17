

class User:

    def __init__(self, data: dict) -> None:
        for name, value in data.items():
            setattr(self, name, value)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"






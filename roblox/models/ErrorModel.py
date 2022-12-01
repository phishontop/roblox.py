

class InvalidUser(Exception):
    """
    Raises Exception when the user the UserFactory is trying to create an invalid user.
    """
    pass


class RateLimit(Exception):
    """
    Raises Exception when request becomes ratelimited.
    """
    pass


class InvalidGroup(Exception):
    """
    Raises Exception when the group is invalid.
    """
    pass

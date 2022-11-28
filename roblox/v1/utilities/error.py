class AuthError(Exception):
    """
    Raises an error when authentication is denied
    Cookie or CRSF token may become expired or invalid
    """
    pass
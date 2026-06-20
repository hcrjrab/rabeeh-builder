from secrets import token_urlsafe


def generate_secret(length: int = 32) -> str:
    return token_urlsafe(length)
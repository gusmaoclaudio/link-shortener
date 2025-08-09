import secrets
import string

_ALPHABET = string.ascii_letters + string.digits + "-_"

def random_slug(length: int = 7) -> str:
    # seguro y URL-friendly
    return "".join(secrets.choice(_ALPHABET) for _ in range(length))

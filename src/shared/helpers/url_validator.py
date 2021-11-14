import string


def url_validate(url: str) -> bool:
    allowed_characters = frozenset(string.ascii_letters + string.digits + '#?-._~%:/')
    return set(url) <= allowed_characters and url.startswith(("http://", "https://"))

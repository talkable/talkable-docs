import os


def get_baseurl() -> str:
    baseurl = os.getenv("BASE_URL", "https://docs.talkable.com")
    stripped_baseurl = f"{baseurl.strip('/')}/"
    return stripped_baseurl

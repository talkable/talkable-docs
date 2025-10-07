import os


def get_baseurl() -> str:
    baseurl = os.getenv("BASE_URL", "")
    stripped_baseurl = f"{baseurl.strip('/')}/"
    return stripped_baseurl

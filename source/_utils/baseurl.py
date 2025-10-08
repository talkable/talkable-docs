import os


def get_baseurl() -> str:
    environment = os.getenv("ENVIRONMENT", "production")
    local_port = os.getenv("LOCAL_PORT", "8080")

    urls = {
        "production": "https://docs.talkable.com/",
        "staging": "https://docs.bastion.talkable.com/",
        "local": f"http://localhost:{local_port}/",
    }

    return urls.get(environment, urls["production"])

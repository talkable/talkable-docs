import os

local_port = os.getenv("LOCAL_PORT")
environment = os.getenv("ENVIRONMENT")
production_host = os.getenv("PRODUCTION_HOST")
staging_host = os.getenv("STAGING_HOST")
development_host = os.getenv("DEVELOPMENT_HOST")

baseurl_json = {
    "development": f"http://{development_host}:{local_port}/",
    "staging": f"https://{staging_host}/",
    "production": f"https://{production_host}/",
}

baseurl = baseurl_json.get(environment)

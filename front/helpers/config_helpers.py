import os


def get_base_url():

    env = os.environ.get("SITE_URL", "test")
    if env.lower() == "test":
        raise Exception(f"url must be set please execute the addpath.ps1")
    return os.environ.get("SITE_URL")

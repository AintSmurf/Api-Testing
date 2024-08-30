import os

API_HOSTS = {
    "test": str(os.environ.get("SITE_URL")) + "/wp-json/wc/v3/",
    "dev": "",
    "prod": "",
}


WOO_API_HOSTS = {"test": str(os.environ.get("SITE_URL")), "dev": "", "prod": ""}


DB_HOSTS = {
    "machine": {"test": os.environ.get("DB_SERVER")},
    "docker": {"test": os.environ.get("DB_SERVER")},
}

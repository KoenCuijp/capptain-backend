from .base import *

SECRET_KEY = "fake-secret-key-for-dev-environment"  # noqa: S105
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "172.18.0.2"]
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "capptain",  # The name of the PostgreSQL database
        "USER": "localhost",  # User for local development
        "PASSWORD": "localhost",  # Password for local development
        "HOST": "capptain-database",  # name of the docker container
        "PORT": "5432",  # Default PostgreSQL port
    }
}

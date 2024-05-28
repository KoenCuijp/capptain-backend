from .base import *

SECRET_KEY = "fake-secret-key-for-dev-environment"  # noqa: S105
ALLOWED_HOSTS = ["localhost", "0.0.0.0"]
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "capptain",  # The name of the postgres database
        "USER": "localhost",  # User for local development
        "PASSWORD": "localhost",  # Password for local development
        "HOST": "capptain-database",  # name of the docker container
        "PORT": "5432",  # Default postgres port
    }
}

# Allow requests from the local frontend
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

"""
Contains the settings for the Capptain project.

decouple.config searches for the secrets in the following order:
    1. Take the secret from an evironment value if it's set there
    2. Take the secret from the .env file (or .ini if your using that)
    3. Take the secret from the default value (2nd parameter of config())

This way we keep secrets out of our codebase and we have the option of overriding
a secret with an environment variable (no strict need to deploy to override a secret).
"""

from pathlib import Path

# Provides easy access to the base path of the project
# It takes the parent.parent.parent directory of this file
BASE_PATH = Path(__file__).resolve().parent.parent.parent

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

ROOT_URLCONF = "capptain.urls"

INSTALLED_APPS = [
    "capptain",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "rest_framework",
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}

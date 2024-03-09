"""
Contains the settings for the Capptain project.

decouple.config searches for the secrets in the following order:
    1. Take the secret from an evironment value if it's set there
    2. Take the secret from the .env file (or .ini if your using that)
    3. Take the secret from the default value (2nd parameter of config())

This way we keep secrets out of our codebase and we have the option of overriding 
a secret with an environment variable (no strict need to deploy to override a secret).
"""

from decouple import config

SECRET_KEY = config("SECRET_KEY")

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

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "www.mysite.com", "172.18.0.2"]
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

from decouple import config as env

from .base import *

SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "172.18.0.2"]  # noqa: S104
DEBUG = True

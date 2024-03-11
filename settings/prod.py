from decouple import config as env

from .base import *

SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = ["www.capptain.com"]
DEBUG = False

from .base import *

from decouple import config as env

SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = ["www.capptain.com"]
DEBUG = False

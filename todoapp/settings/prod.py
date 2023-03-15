from .settings import *
import dj_database_url
import environ
import os

env = environ.Env()
environ.Env().read_env()
DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = []
DATABASES = {
    'default': dj_database_url.parse(env('DATABASE_URL'))
}

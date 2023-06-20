from .settings import *
import dj_database_url
import environ
import os

env = environ.Env()
environ.Env().read_env()
DEBUG = True
SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = ['todobackendjune.onrender.com']
DATABASES = {
    'default': dj_database_url.parse(env('DATABASE_URL'))
}

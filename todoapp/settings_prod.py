import dj_database_url
import environ

env = environ.Env()
environ.Env().read_env()
SECRET_KEY = 'django-insecure-^))%5(p=50!u03t6qu0fjryj94gbh2g3&s=sm^j6po(mzq-%qi'
DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': dj_database_url.parse(env('DATABASE_URL'))
}

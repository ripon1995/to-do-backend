from .settings import *

DEBUG = True
SECRET_KEY = 'django-insecure-^))%5(p=50!u03t6qu0fjryj94gbh2g3&s=sm^j6po(mzq-%qi'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todo',
        'USER': 'postgres',
        'PASSWORD': 'rootless',
        'HOST': 'localhost',
        'PORT': '',
    }
}

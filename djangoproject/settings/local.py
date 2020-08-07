from .base import *


DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'djangodb',
        'USER': 'postgres',
        'PASSWORD': 'Tomin@123',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
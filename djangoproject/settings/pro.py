from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

ADMINS = (
('Tomin', 'tominjose222@gmail.com'),
)



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'djangodb',
        'USER': 'postgres',
        'PASSWORD': 'Tomin@123',
        'HOST': 'localhost',
        'PORT': '5432'
    }
} 
from .base import *

DEBUG = False
ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3', 
    'NAME': config('DB_NAME'),
    'USER': config('DB_USER'),
    'PASSWORD': config('DB_PASSWORD'),
    'HOST': config('DB_HOST'),
    'PORT': config('DB_PORT', default=5432, cast=int),
}

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
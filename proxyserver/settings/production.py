"""
Settings used ONLY on development environment
"""

# SECURITY WARNING: don't run with debug turned on in production!
import os

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'proxy',
        'USER': 'root',
        'PASSWORD': 'X9BlOVKbG3',
        'HOST': 'localhost',
    }
}

SITE_DOMAIN = 'http://proxy-service.instandart.com'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# Application definition

here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
PROJECT_ROOT = os.path.realpath(here(".."))
root = lambda *x: os.path.realpath(os.path.join(os.path.abspath(PROJECT_ROOT), *x))

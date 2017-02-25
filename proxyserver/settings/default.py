"""
Settings shared between both production and development environment
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from kombu import Exchange, Queue
from celery.schedules import crontab

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q2r%d@rv)p=!acic3a9b!-h_@#dbu$#*(!p%_beez3+=)ovqmy'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'proxy-service.instandart.com', '67.205.186.116']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_countries',
    'rest_framework',
    'proxyserver.apps.core',
    'proxyserver.apps.authorization',
    'proxyserver.apps.api',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware'
)

AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'books',
        'USER': 'root',
        'PASSWORD': 'X9BlOVKbG3',
        'HOST': 'localhost',
        'PORT': '5432',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        }
    }
}

ROOT_URLCONF = 'proxyserver.urls'

COUNTRIES_OVERRIDE = {
    'EU': 'Europe Union',
    'UD': 'Undefined'
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'proxyserver.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
PROJECT_ROOT = os.path.realpath(here(".."))
root = lambda *x: os.path.realpath(os.path.join(os.path.abspath(PROJECT_ROOT), *x))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = root('static_root')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


LOGIN_REDIRECT_URL = '/home/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'


# CELERY SETTINGS
BROKER_URL = 'amqp://guest:guest@rabbitmq:5672//'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'amqp://guest@rabbitmq//'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ALWAYS_EAGER = False
CELERYD_MAX_TASKS_PER_CHILD = 4
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE_TYPE = 'default'
CELERY_DEFAULT_ROUTING_KEY = 'default'

# here will be scheduled tasks
CELERYBEAT_SCHEDULE = {
    'add_proxy': {
        'task': 'proxyserver.apps.core.tasks.add_proxy_to_db',
        'schedule': crontab(minute='*/3')
    },
    'check_proxy': {
        'task': 'proxyserver.apps.core.tasks.check_task',
        'schedule': crontab(minute='*/10')
    }
}

CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('proxy_finder', Exchange('proxy_finder'), routing_key='proxy_finder'),
    Queue('proxy_checker', Exchange('proxy_checker'), routing_key='proxy_checker'),
)

# here will be routes for tasks to queue
CELERY_ROUTES = {
    'proxyserver.apps.core.tasks.add_proxy_to_db': {
        'queue': 'proxy_finder',
        'routing_key': 'proxy_finder'
    },
    'proxyserver.apps.core.tasks.check_task': {
        'queue': 'proxy_checker',
        'routing_key': 'proxy_checker'
    },
}
import os
from kombu import Queue, Exchange
from celery.schedules import crontab
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1wkp6^g)_9@q90vu-hwcb2=+yjkfhp968!d!5v%g97w9qol^ly'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'proxy-service.instandart.com', '67.205.186.116']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_countries',
    'rest_framework',
    'proxyserver.apps.core',
    'proxyserver.apps.authorization',
    'proxyserver.apps.api',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proxyserver.urls'

COUNTRIES_OVERRIDE = {
    'EU': 'Europe Union',
    'UD': 'Undefined'
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'static'),
                 os.path.join(BASE_DIR, 'static_root')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'proxyserver.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
PROJECT_ROOT = os.path.realpath(here(".."))
root = lambda *x: os.path.realpath(os.path.join(os.path.abspath(PROJECT_ROOT), *x))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = BASE_DIR + '/static_root'

STATIC_URL = '/static/'

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

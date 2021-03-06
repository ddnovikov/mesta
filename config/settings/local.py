from .base import *


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mesta',
        'USER': 'mesta_app',
        'PASSWORD': get_env_variable('MESTA_DB_PWD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'mesta' / 'media_cdn'
STATIC_ROOT = BASE_DIR / 'mesta' / 'static_cdn'

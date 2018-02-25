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

SECRET_KEY = get_env_variable('MESTA_SECRET_KEY')

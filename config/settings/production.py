from .base import *
import dj_database_url


DEBUG = False

CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 1000000
SECURE_FRAME_DENY = True
ALLOWED_HOSTS =  ['mesta-project.herokuapp.com']


# MIDDLEWARE += [
#     'whitenoise.middleware.WhiteNoiseMiddleware',
# ]

INSTALLED_APPS += ['storages']

db_from_env = dj_database_url.config(conn_max_age=500)

DATABASES = {
    'default': db_from_env
}

# MEDIA_ROOT = BASE_DIR / 'mesta' / 'media_cdn'
# STATIC_ROOT = BASE_DIR / 'mesta' / 'static_cdn'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
    },
}

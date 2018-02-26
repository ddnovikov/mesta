from .base import get_env_variable

if get_env_variable('ENVIRONMENT') == 'prod':
    from .production import *
    from .aws import *
elif get_env_variable('ENVIRONMENT') == 'local':
    from .local import *

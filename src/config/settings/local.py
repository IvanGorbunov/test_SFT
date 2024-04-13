from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', True)
SQL_DEBUG = env.bool('SQL_DEBUG', True)
RUN_IN_DOCKER = env.bool('RUN_IN_DOCKER', False)


if SQL_DEBUG:
    MIDDLEWARE = MIDDLEWARE + ['utils.middleware.DebugQuerysetsWare']
if DEBUG:
    MIDDLEWARE = MIDDLEWARE + ['debug_toolbar.middleware.DebugToolbarMiddleware',]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
        'default': env.db(var='DATABASE_URL_IN_DOCKER') if RUN_IN_DOCKER else env.db(),
}

if DEBUG:
    import socket
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

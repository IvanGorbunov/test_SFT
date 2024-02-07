from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
SQL_DEBUG = False
RUN_IN_DOCKER = True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
        'default': env.db(var='DATABASE_URL_IN_DOCKER') if RUN_IN_DOCKER else env.db(),
}

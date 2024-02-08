from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
SQL_DEBUG = False
RUN_IN_DOCKER = env.bool('RUN_IN_DOCKER', True)

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': env.str('SQL_ENGINE', 'django.db.backends.sqlite3'),
            'NAME': env.str('SQL_DATABASE', os.path.join(BASE_DIR, "../db.sqlite3")),
            'USER': env.str('SQL_USER', 'user'),
            'PASSWORD': env.str('SQL_PASSWORD', 'password'),
            'HOST': env.str('SQL_HOST', 'localhost'),
            'PORT': env.str('SQL_PORT', '5432'),
        }
}

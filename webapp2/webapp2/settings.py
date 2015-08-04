# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ty#6j$h&i=)t$o^ea4uzx4-8kww1=(^6k*2k5hlv^#^$db1_b!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    #
    'squares',
    'users',
    #
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
)

ROOT_URLCONF = 'webapp2.urls'


WSGI_APPLICATION = 'webapp2.wsgi.application'


#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'webapp2',
#        'USER': 'root',
#        'PASSWORD': 'playinghard',
#        'HOST': '127.0.0.1',
#        'PORT': '3306',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webapp2',
        'USER': 'cdb_outerroot',
        'PASSWORD': 'Moment!x',
        'HOST': '55a9b6fa55ab1.sh.cdb.myqcloud.com',
        'PORT': '6633',
        'CONN_MAX_AGE': None,
    }
}

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#
AUTH_USER_MODEL = 'users.Users'

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)



BROKER_URL = 'amqp://guest:guest@rabbitmq:5672//'
# BROKER_URL = 'amqp://guest@localhost//'
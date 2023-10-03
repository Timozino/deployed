import os


from pathlib import Path


from dotenv import load_dotenv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY='w7a8555a@lj8nax7tem0caa2f2rjm2ahsascyf83sa5alyv68vea'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['technokraftzonline.azurewebsites.net', 'technokraftz.com', '*']


#CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS').split(' ')


# SECURE_SSL_REDIRECT = \
#     os.getenv('SECURE_SSL_REDIRECT', '0').lower() in ['true', 't', '1']
# if SECURE_SSL_REDIRECT:
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = [
    "jazzmin",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'user',
    'bootstrap4',
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'app.middleware.AdBlockerMiddleware',
    'django.contrib.staticfiles.middleware.StaticFilesMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'LMS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Lagos"

USE_I18N = True

USE_TZ = True

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

#static_or_media_list=['/static/', '/media/']
# static_files_list=[os.path.join(BASE_DIR, 'static')]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



# MEDIA_URL=static_or_media_list[1]
# MEDIA_ROOT=MEDIA_URL
# MEDIA_URL = 'media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

AUTHENTICATION_BACKENDS = [
#    'app.emailBackend.EmailBackEnd',
#    # Add other authentication backends if needed
    'django.contrib.auth.backends.ModelBackend',  # Default backend for username/password authentication
]

ADMIN_URL="supersecret/"
#AUTH_USER_MODEL = 'app.User'

JAZZMIN_SETTINGS={
    "site_header":"Technokraftz Academy",
    "site_brand":"Technokraftz",
    "site_logo":"assets/img/technok/technok.png",
    "copyright":"All Right Reserved, Copyright 2023-Till Date",
    "order_with_respect_to":["Technokraftz"]
}
LOGIN_REDIRECT_URL = 'home'
# LOGIN_URL='login/'
#LOGOUT_REDIRECT_URL = 'login'
AUTH_USER_MODEL = 'auth.User'




EMAIL_BACKEND = ['django.core.mail.backends.smtp.EmailBackend','django.core.mail.backends.console.EmailBackend']
EMAIL_HOST = 'mailhog'  # Use the service name defined in docker-compose.yml
EMAIL_PORT = 1025  # The SMTP port exposed by MailHog


CRISPY_TEMPLATE_PACK = 'bootstrap4'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

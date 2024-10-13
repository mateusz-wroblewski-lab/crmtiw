from .base import *
import os


SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)

ROOT_URLCONF = 'core.urls'

# Host
ALLOWED_HOSTS = ['localhost', 'crmtiw.onrender.com', 'crmtiw.studioshouse.com', 'www.crmtiw.studioshouse.com']
CSRF_TRUSTED_ORIGINS = ['https://crmtiw.onrender.com', 'https://crmtiw.studioshouse.com', 'http://crmtiw.studioshouse.com']


#X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 86400
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# SECURE_SSL_REDIRECT = False # if True "You're accessing the development server over HTTPS, but it only supports HTTP."

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_AGE = 300
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

AUTO_LOGOUT = {
    'IDLE_TIME': 300,
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
    'MESSAGE': 'Sesja wygasła. Proszę zalogować się ponownie.',
    } 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crm',
    'management',
    'patients',

    'fontawesomefree',

    'turnstile',
    
    'dbbackup',

]

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR / 'core/db/backup'}


DATABASES = { 
    # Local database
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DBU'), # name of databsae
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    },

    # Neon database
    'neon_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('PGDATABASE'),
        'USER': env('PGUSER'),
        'PASSWORD': env('PGPASSWORD'),
        'HOST': env('PGHOST'),
        'PORT': 5432,
        'OPTIONS': {'sslmode': 'require',},
    },
}

DATABASE_ROUTERS = [
    # 'core.settings.routers.CloudAppRouter',
    # 'core.settings.routers.LocalAppRouter',
    'core.settings.routers.NeonAppRouter',
    ]

# Cloudflare
TURNSTILE_SITEKEY = env('TURNSTILE_SITEKEY')
TURNSTILE_SECRET = env('TURNSTILE_SECRET')
TURNSTILE_JS_API_URL = 'https://challenges.cloudflare.com/turnstile/v0/api.js'
TURNSTILE_VERIFY_URL = 'https://challenges.cloudflare.com/turnstile/v0/siteverify'
TURNSTILE_TIMEOUT = 5

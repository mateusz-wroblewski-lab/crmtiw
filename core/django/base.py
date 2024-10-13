import os

from core.env import BASE_DIR, env

env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = ["*"]

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
    'phonenumber_field',

    'django_recaptcha',
    'turnstile',
    'login_history',

    'django_apscheduler',
    'dbbackup',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'login_required.middleware.LoginRequiredMiddleware',
    
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_auto_logout.middleware.auto_logout', # Django auto logout (1)

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                                
                'django_auto_logout.context_processors.auto_logout_client', # Django auto logout (2)
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'core/db/db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'core/static')
STATIC_URL = 'core/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'home'

AUTO_LOGOUT = {
    'IDLE_TIME': 300,
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
    'MESSAGE': 'Sesja wygasła. Proszę zalogować się ponownie.',
    } 

SESSION_COOKIE_AGE = 300
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# backend/settings.py

import os
from pathlib import Path
from datetime import timedelta

# BASE_DIR is the directory where manage.py is located
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')

DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
        'django.contrib.auth',
            'django.contrib.contenttypes',
                'django.contrib.sessions',
                    'django.contrib.messages',
                        'django.contrib.staticfiles',
                            'rest_framework',
                                'rest_framework_simplejwt',
                                    'corsheaders',
                                        'users',
                                            'products',
                                                'orders',
                                                    'cart',
                                                        'payments',
                                                            'reviews',
                                                                'coupons',
                                                                    'core',
                                                                    ]

                                                                    MIDDLEWARE = [
                                                                        'corsheaders.middleware.CorsMiddleware',
                                                                            'django.middleware.security.SecurityMiddleware',
                                                                                'django.contrib.sessions.middleware.SessionMiddleware',
                                                                                    'django.middleware.common.CommonMiddleware',
                                                                                        'django.middleware.csrf.CsrfViewMiddleware',
                                                                                            'django.contrib.auth.middleware.AuthenticationMiddleware',
                                                                                                'django.contrib.messages.middleware.MessageMiddleware',
                                                                                                    'django.middleware.clickjacking.XFrameOptionsMiddleware',
                                                                                                    ]

                                                                                                    ROOT_URLCONF = 'backend.urls'

                                                                                                    TEMPLATES = [
                                                                                                        {
                                                                                                                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                                                                                                                        'DIRS': [BASE_DIR / 'templates'],
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

                                                                                                                                                                                                                                            WSGI_APPLICATION = 'backend.wsgi.application'

                                                                                                                                                                                                                                            DATABASES = {
                                                                                                                                                                                                                                                'default': {
                                                                                                                                                                                                                                                        'ENGINE': 'django.db.backends.postgresql',
                                                                                                                                                                                                                                                                'NAME': os.getenv('DB_NAME', 'ecommerce_db'),
                                                                                                                                                                                                                                                                        'USER': os.getenv('DB_USER', 'user'),
                                                                                                                                                                                                                                                                                'PASSWORD': os.getenv('DB_PASSWORD', 'password'),
                                                                                                                                                                                                                                                                                        'HOST': os.getenv('DB_HOST', 'localhost'),
                                                                                                                                                                                                                                                                                                'PORT': os.getenv('DB_PORT', '5432'),
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

                                                                                                                                                                                                                                                                                                                                                                    TIME_ZONE = 'UTC'

                                                                                                                                                                                                                                                                                                                                                                    USE_I18N = True

                                                                                                                                                                                                                                                                                                                                                                    USE_L10N = True

                                                                                                                                                                                                                                                                                                                                                                    USE_TZ = True

                                                                                                                                                                                                                                                                                                                                                                    STATIC_URL = '/static                                                                                                                                                                                                                                                                                                                                                                                     'ALGORITHM': 'HS# backend/settings.py

import os
from pathlib import Path
from datetime import timedelta

# BASE_DIR is the directory where manage.py is located
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')

DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'users',
    'products',
    'orders',
    'cart',
    'payments',
    'reviews',
    'coupons',
    'core',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'ecommerce_db'),
        'USER': os.getenv('DB_USER', 'user'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'password'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS Settings
CORS_ALLOW_ALL_ORIGINS = True

# JWT Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
}

# Custom user model (if using a custom model)
AUTH_USER_MODEL = 'users.User'# backend/settings.py

import os
from pathlib import Path
from datetime import timedelta

# BASE_DIR is the directory where manage.py is located
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')

DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'users',
    'products',
    'orders',
    'cart',
    'payments',
    'reviews',
    'coupons',
    'core',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'ecommerce_db'),
        'USER': os.getenv('DB_USER', 'user'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'password'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS Settings
CORS_ALLOW_ALL_ORIGINS = True

# JWT Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
}

# Custom user model (if using a custom model)
AUTH_USER_MODEL = 'users.User'
                                                                                                                                                                                                                                                                                                                                                                                            'SIGNING_KEY': SECRET_KEY,
                                                                                                                                                                                                                                                                                                                                                                                                'VERIFYING_KEY': None,
                                                                                                                                                                                                                                                                                                                                                                                                    'AUDIENCE': None,
                                                                                                                                                                                                                                                                                                                                                                                                        'ISSUER': None,
                                                                                                                                                                                                                                                                                                                                                                                                            'JWK_URL': None,
                                                                                                                                                                                                                                                                                                                                                                                                            }

                                                                                                                                                                                                                                                                                                                                                                                                            # Custom user model (if using a custom model)
                                                                                                                                                                                                                                                                                                                                                                                                            AUTH_USER_MODEL = 'users.User'
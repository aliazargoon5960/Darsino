from pathlib import Path
import os
import dj_database_url  # برای سازگاری دیتابیس با Render

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------
# SECURITY SETTINGS
# -------------------
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-7o=v4oj&p%w(2d&ha+-s4z1(^)mgovl1ex9m!b8b4s_&2xxt3z")
DEBUG = os.environ.get("DEBUG", "True") == "True"
ALLOWED_HOSTS = ["*"]

# -------------------
# INSTALLED APPS
# -------------------
INSTALLED_APPS = [
    'admin_persian',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # my apps
    'account_module',
    'home_module',
    'contact_module',
    'course_module',
    'blog_module',
    'site_module',
    'cart_module',
    'user_panel_module',
    'tickets_module',
    'admin_panel',

    # 3rd party
    'widget_tweaks',
    'django_cleanup.apps.CleanupConfig',
    'django.contrib.humanize',
    'cloudinary',
    'cloudinary_storage',
]

# -------------------
# MIDDLEWARE
# -------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
ROOT_URLCONF = 'Darsino.urls'

# -------------------
# TEMPLATES
# -------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'context_processors.context_processors.site_footer',
            ],
        },
    },
]

WSGI_APPLICATION = 'Darsino.wsgi.application'

# -------------------
# DATABASE
# -------------------
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'Darsino.sqlite3'}",
        conn_max_age=600
    )
}

# -------------------
# PASSWORD VALIDATION
# -------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# -------------------
# INTERNATIONALIZATION
# -------------------
LANGUAGE_CODE = 'fa-ir'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------
# STATIC & MEDIA FILES
# -------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 🔹 از Cloudinary برای مدیا استفاده می‌کنیم، پس نیازی به MEDIA_ROOT نیست
MEDIA_URL = '/media/'

# -------------------
# CLOUDINARY CONFIG
# -------------------
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': "devswomrd",
    'API_KEY': "799598748177243",
    'API_SECRET': "6g4cn9wCbsb4qaswk5OzW_lHKxg",
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# -------------------
# OTHER SETTINGS
# -------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_URL = '/account/login'
APPEND_SLASH = True
AUTH_USER_MODEL = 'account_module.User'

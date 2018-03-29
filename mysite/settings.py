import os  # isort:skip
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/



WSGI details information: https://www.python.org/dev/peps/pep-0333/#middleware-components-that-play-both-sides
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yo%_k!%&6&zrz1#k_kd@am17bn_98y0$^n@9u9d12wvpy%fwv8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ "35.200.81.59","localhost","127.0.0.1"]


# Application definition



ROOT_URLCONF = 'mysite.urls'




# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'
# 
USE_I18N = True
# 
# USE_L10N = True
# 
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

# CKEDITOR_UPLOAD_PATH = "C:/Users/shikw/ENV/mysite/"
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': "100%",
    },
}

 
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'mysite', 'static'),
    os.path.join(BASE_DIR, 'firstsite', 'static'),
    os.path.join(BASE_DIR, 'mycareer', ''),
)

SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'firstsite', 'templates'),
                 os.path.join(BASE_DIR, 'greetplugin', 'templates'),
                 os.path.join(BASE_DIR, 'mysite', 'templates'),
                 os.path.join(BASE_DIR, 'mycareer', 'templates')
                 
                 ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'firstsite.context_processor.share_vars',
#                 'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]


# wiring my own middlerware :https://simpleisbetterthancomplex.com/tutorial/2016/07/18/how-to-create-a-custom-django-middleware.html
MIDDLEWARE = (
#     'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'cms.middleware.user.CurrentUserMiddleware',
#     'cms.middleware.page.CurrentPageMiddleware',
#     'cms.middleware.toolbar.ToolbarMiddleware',
#     'cms.middleware.language.LanguageCookieMiddleware'
)

INSTALLED_APPS = (
#     'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
#     'cms',
#     'menus',
#     'sekizai',
#     'treebeard',
#     'djangocms_text_ckeditor',
#     'filer',
#     'easy_thumbnails',
#     'djangocms_column',
#     'djangocms_file',
#     'djangocms_link',
#     'djangocms_picture',
#     'djangocms_style',
#     'djangocms_snippet',
#     'djangocms_googlemap',
#     'djangocms_video',
#     'aldryn_bootstrap3',
    'mysite',
#     "greetplugin",
    "firstsite",
    "mycareer",
    "ckeditor",
    "ckeditor_uploader"
#     "tinymce",
)

# LANGUAGES = (
#     ## Customize this
#     ('ja', gettext('ja')),
#     ('zh', ("simple chinese"))),
# )

# CMS_LANGUAGES = {
#     ## Customize this
#     1: [
#         {
#             'code': 'ja',
#             'name': gettext('ja'),
#             'redirect_on_fallback': True,
#             'public': True,
#             'hide_untranslated': False,
#         },
#     ],
#     'default': {
#         'redirect_on_fallback': True,
#         'public': True,
#         'hide_untranslated': False,
#     },
# }
# 
# CMS_TEMPLATES = (
#     ## Customize this
#     ('fullwidth.html', 'Fullwidth'),
#     ('sidebar_left.html', 'Sidebar Left'),
#     ('sidebar_right.html', 'Sidebar Right')
# )
# 
# CMS_PERMISSION = True
# 
# CMS_PLACEHOLDER_CONF = {}


# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'full',
#         "allowedContent":{
#             "script": "true",
#         }
#     }
# }


DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

LACALE_PATH = {
    os.path.join(BASE_DIR,"locale")
}

MIGRATION_MODULES = {
    
}



THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

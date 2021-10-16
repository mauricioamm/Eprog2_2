"""
Django settings for EprogProj project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zzmmc^p&-elo^1hod1@fo$u(srx15@*z+d$q7kxg%-%7mv!zob'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'EprogApp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'EprogProj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates', 'templates/EprogApp',
                              'EprogApp/templates/EprogApp','EprogApp/templates/registration')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'EprogProj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),},
    'mauricioamm': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'mauricioamm.sqlite3'), },

'neuro_p1' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p1.sqlite3'), },
'neuro_p2' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p2.sqlite3'), },
'neuro_p3' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p3.sqlite3'), },
'neuro_p4' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p4.sqlite3'), },
'neuro_p5' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p5.sqlite3'), },
'neuro_p6' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p6.sqlite3'), },
'neuro_p7' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p7.sqlite3'), },
'neuro_p8' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p8.sqlite3'), },
'neuro_p9' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p9.sqlite3'), },
'neuro_p10' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p10.sqlite3'), },
'neuro_p11' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p11.sqlite3'), },
'neuro_p12' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p12.sqlite3'), },
'neuro_p13' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p13.sqlite3'), },
'neuro_p14' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p14.sqlite3'), },
'neuro_p15' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p15.sqlite3'), },
'neuro_p16' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p16.sqlite3'), },
'neuro_p17' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p17.sqlite3'), },
'neuro_p18' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p18.sqlite3'), },
'neuro_p19' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p19.sqlite3'), },
'neuro_p20' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p20.sqlite3'), },
'neuro_p21' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p21.sqlite3'), },
'neuro_p22' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p22.sqlite3'), },
'neuro_p23' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p23.sqlite3'), },
'neuro_p24' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p24.sqlite3'), },
'neuro_p25' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p25.sqlite3'), },
'neuro_p26' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p26.sqlite3'), },
'neuro_p27' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p27.sqlite3'), },
'neuro_p28' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p28.sqlite3'), },
'neuro_p29' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p29.sqlite3'), },
'neuro_p30' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p30.sqlite3'), },
'neuro_p31' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p31.sqlite3'), },
'neuro_p32' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p32.sqlite3'), },
'neuro_p33' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p33.sqlite3'), },
'neuro_p34' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p34.sqlite3'), },
'neuro_p35' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p35.sqlite3'), },
'neuro_p36' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p36.sqlite3'), },
'neuro_p37' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p37.sqlite3'), },
'neuro_p38' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p38.sqlite3'), },
'neuro_p39' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p39.sqlite3'), },
'neuro_p40' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p40.sqlite3'), },
'neuro_p' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'neuro_p.sqlite3'), },

'ac_p1' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p1.sqlite3'), },
'ac_p2' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p2.sqlite3'), },
'ac_p3' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p3.sqlite3'), },
'ac_p4' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p4.sqlite3'), },
'ac_p5' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p5.sqlite3'), },
'ac_p6' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p6.sqlite3'), },
'ac_p7' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p7.sqlite3'), },
'ac_p8' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p8.sqlite3'), },
'ac_p9' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p9.sqlite3'), },
'ac_p10' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p10.sqlite3'), },
'ac_p11' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p11.sqlite3'), },
'ac_p12' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p12.sqlite3'), },
'ac_p13' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p13.sqlite3'), },
'ac_p14' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p14.sqlite3'), },
'ac_p15' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p15.sqlite3'), },
'ac_p16' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p16.sqlite3'), },
'ac_p17' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p17.sqlite3'), },
'ac_p18' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p18.sqlite3'), },
'ac_p19' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p19.sqlite3'), },
'ac_p20' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p20.sqlite3'), },
'ac_p21' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p21.sqlite3'), },
'ac_p22' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p22.sqlite3'), },
'ac_p23' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p23.sqlite3'), },
'ac_p24' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p24.sqlite3'), },
'ac_p25' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p25.sqlite3'), },
'ac_p26' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p26.sqlite3'), },
'ac_p27' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p27.sqlite3'), },
'ac_p28' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p28.sqlite3'), },
'ac_p29' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p29.sqlite3'), },
'ac_p30' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p30.sqlite3'), },
'ac_p' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'ac_p.sqlite3'), },

'biologia_p1' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p1.sqlite3'), },
'biologia_p2' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p2.sqlite3'), },
'biologia_p3' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p3.sqlite3'), },
'biologia_p4' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p4.sqlite3'), },
'biologia_p5' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p5.sqlite3'), },
'biologia_p6' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p6.sqlite3'), },
'biologia_p7' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p7.sqlite3'), },
'biologia_p8' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p8.sqlite3'), },
'biologia_p9' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p9.sqlite3'), },
'biologia_p10' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p10.sqlite3'), },
'biologia_p11' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p11.sqlite3'), },
'biologia_p12' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p12.sqlite3'), },
'biologia_p13' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p13.sqlite3'), },
'biologia_p14' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p14.sqlite3'), },
'biologia_p15' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p15.sqlite3'), },
'biologia_p16' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p16.sqlite3'), },
'biologia_p17' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p17.sqlite3'), },
'biologia_p18' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p18.sqlite3'), },
'biologia_p19' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p19.sqlite3'), },
'biologia_p20' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p20.sqlite3'), },
'biologia_p21' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p21.sqlite3'), },
'biologia_p22' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p22.sqlite3'), },
'biologia_p23' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p23.sqlite3'), },
'biologia_p24' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p24.sqlite3'), },
'biologia_p25' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p25.sqlite3'), },
'biologia_p' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'biologia_p.sqlite3'), },

'geografia_p1' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p1.sqlite3'), },
'geografia_p2' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p2.sqlite3'), },
'geografia_p3' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p3.sqlite3'), },
'geografia_p4' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p4.sqlite3'), },
'geografia_p5' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p5.sqlite3'), },
'geografia_p6' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p6.sqlite3'), },
'geografia_p7' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p7.sqlite3'), },
'geografia_p8' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p8.sqlite3'), },
'geografia_p9' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p9.sqlite3'), },
'geografia_p10' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p10.sqlite3'), },
'geografia_p11' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p11.sqlite3'), },
'geografia_p12' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p12.sqlite3'), },
'geografia_p13' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p13.sqlite3'), },
'geografia_p14' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p14.sqlite3'), },
'geografia_p15' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p15.sqlite3'), },
'geografia_p16' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p16.sqlite3'), },
'geografia_p17' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p17.sqlite3'), },
'geografia_p18' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p18.sqlite3'), },
'geografia_p19' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p19.sqlite3'), },
'geografia_p20' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p20.sqlite3'), },
'geografia_p21' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p21.sqlite3'), },
'geografia_p22' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p22.sqlite3'), },
'geografia_p23' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p23.sqlite3'), },
'geografia_p24' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p24.sqlite3'), },
'geografia_p25' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p25.sqlite3'), },
'geografia_p' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'geografia_p.sqlite3'), },

'historia_p1' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p1.sqlite3'), },
'historia_p2' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p2.sqlite3'), },
'historia_p3' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p3.sqlite3'), },
'historia_p4' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p4.sqlite3'), },
'historia_p5' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p5.sqlite3'), },
'historia_p6' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p6.sqlite3'), },
'historia_p7' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p7.sqlite3'), },
'historia_p8' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p8.sqlite3'), },
'historia_p9' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p9.sqlite3'), },
'historia_p10' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p10.sqlite3'), },
'historia_p11' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p11.sqlite3'), },
'historia_p12' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p12.sqlite3'), },
'historia_p13' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p13.sqlite3'), },
'historia_p14' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p14.sqlite3'), },
'historia_p15' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p15.sqlite3'), },
'historia_p16' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p16.sqlite3'), },
'historia_p17' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p17.sqlite3'), },
'historia_p18' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p18.sqlite3'), },
'historia_p19' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p19.sqlite3'), },
'historia_p20' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p20.sqlite3'), },
'historia_p21' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p21.sqlite3'), },
'historia_p22' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p22.sqlite3'), },
'historia_p23' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p23.sqlite3'), },
'historia_p24' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p24.sqlite3'), },
'historia_p25' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p25.sqlite3'), },
'historia_p' : {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'historia_p.sqlite3'), },


    #no admin, dar como sobrenome aos cadastrados: p1, p2, p3, p4...
     }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/'

#LOGOUT_REDIRECT_URL = '/accounts/login'
LOGOUT_REDIRECT_URL = 'url_Entrada_login'
STATIC_ROOT = '/home/mauricioamm/mauricioamm.pythonanywhere.com/EprogApp/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')  # 'media' is my media folder
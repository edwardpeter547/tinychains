import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables.
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY") or ""

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG") == "True"

# ALLOWED HOST: This should be set when DEBUG=False
ALLOWED_HOSTS = []
HOST_LIST = os.getenv("ALLOWED_HOSTS")
if HOST_LIST:
    ALLOWED_HOSTS = HOST_LIST.split(",")

PORT = os.getenv("PORT") or 8000


# DJANGO APPS: The default django apps.
CORE_DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

# CUSTOM APPS: Tinychains core apps.
TINYCHAINS_APPS = [
    "shared",
]

# DJANGO MIDDLEWARE: The default django middleware
CORE_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# TINYCHAINS MIDDLEWARE: The tinychains specific middlewares
TINYCHAINS_MIDDLEWARE = []

# DATABASE SETUP: This configuration uses a development sqlite
# whenever DEBUG=True, else uses a production postgresql datasource.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3' if DEBUG else 'django.db.backends.postgresql',
        'NAME': BASE_DIR / os.getenv("DATABASE_NAME", "db.sqlite3"),
        'USER': os.getenv("DATABASE_USER", ""),
        'PASSWORD': os.getenv("DATABASE_PASSWORD", ""),
        'HOST': os.getenv("DATABASE_HOST", ""),
        'PORT': os.getenv("DATABASE_PORT", ""),
    }
}
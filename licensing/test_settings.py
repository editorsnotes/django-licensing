DEBUG=True

DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

SECRET_KEY = 'secret'

INSTALLED_APPS=(
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'licensing',
    'tests',
)

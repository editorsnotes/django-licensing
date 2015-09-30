#!/usr/bin/env python
# original code from <http://stackoverflow.com/questions/3841725/how-to-launch-tests-for-django-reusable-app>
import os, sys
from django.conf import settings
import django


settings.configure(DEBUG=True,
               DATABASES={
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                    }
                },
               #ROOT_URLCONF='myapp.urls',
               INSTALLED_APPS=('django.contrib.auth',
                              'django.contrib.contenttypes',
                              'django.contrib.sessions',
                              'django.contrib.admin',
                              'licensing',
                              'tests',))

try:
    # Django <= 1.8
    from django.test.simple import DjangoTestSuiteRunner
    test_runner = DjangoTestSuiteRunner(verbosity=1)
except ImportError:
    # Django >= 1.8
    from django.test.runner import DiscoverRunner
    test_runner = DiscoverRunner(verbosity=1)

# otherwise we get an 'Apps not loaded yet' error
if hasattr(django, 'setup'):
    django.setup()

failures = test_runner.run_tests(['tests'])
if failures:
    sys.exit(failures)
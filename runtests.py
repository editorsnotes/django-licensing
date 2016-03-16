#!/usr/bin/env python

# original code from <http://stackoverflow.com/questions/3841725/>

import os
import sys
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'licensing.test_settings'

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

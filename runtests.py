#!/usr/bin/env python

import os
import sys

import django
from django.test.runner import DiscoverRunner

os.environ['DJANGO_SETTINGS_MODULE'] = 'licensing.test_settings'

django.setup()
test_runner = DiscoverRunner(verbosity=1)
failures = test_runner.run_tests(['tests'])

if failures:
    sys.exit(failures)

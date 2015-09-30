"""

"""

from django.test import TestCase

# https://github.com/Beeblio/django-vote
from licensing.models import License
from .models import Whatever


class SubclassTests(TestCase):
    def test_save(self):
        whatever = Whatever(license_id=1)
        whatever.save()

class LicenseTests(TestCase):
    def test_save(self):
        n_before = License.objects.all().count()

        license = License(name='foobar', symbols=u'\xf0\x9f\x92\xa9', url='http://example.com')
        license.full_clean() # https://code.djangoproject.com/ticket/13100
        license.save()

        n_after = License.objects.all().count()

        self.assertEqual(n_after, n_before + 1)
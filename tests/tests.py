# encoding: utf-8
"""

"""

from django.test import TestCase

# https://github.com/Beeblio/django-vote
from licensing.models import License
from .models import Whatever
from django.template import Template, Context, TemplateDoesNotExist
from django.shortcuts import render_to_response


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

class TemplateTagsTests(TestCase):
    def _get_random_template(self):
        return License.objects.order_by('?').first()

    def test_default_template(self):
        license = License.objects.get(pk=1) # no random, we need a known symbol
        html = '''{% load licensing_tags %}{% show_license license %}'''
        template = Template(html)
        render = template.render(Context({'license': license}))

        self.assertEqual(render, u'<i class="openwebicon">©</i>', 'Failed to render known license')

    def test_not_existing_template(self):
        license = self._get_random_template()
        html = '''{% load licensing_tags %}{% show_license license template="idontexist.html" %}'''
        template = Template(html)

        with self.assertRaisesMessage(TemplateDoesNotExist, ''):
            template.render(Context({'license': license}))

    def test_custom_template(self):
        license = self._get_random_template()
        html = '''{% load licensing_tags %}{% show_license license template="tests/dummy.html" %}'''
        template = Template(html)

        render = template.render(Context({'license': license}))

        self.assertEqual(render, 'FOObar')

    def test_setup_css(self):

        with self.assertTemplateUsed('licensing/setup.html'):
            render = render_to_response('tests/test_setup.html')

    def test_setup_custom_class_css(self):
        render = None

        with self.assertTemplateUsed('licensing/setup.html'):
            render = render_to_response('tests/test_setup_custom.html')

        self.assertContains(render, 'foobar')

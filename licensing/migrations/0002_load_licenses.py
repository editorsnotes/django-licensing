# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.core.management import call_command


def load_license_fixture(apps, schema_editor):
    call_command('loaddata', 'initial_data.json', app_label='licensing')


class Migration(migrations.Migration):

    dependencies = [
        ('licensing', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_license_fixture)
    ]

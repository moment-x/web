# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20150725_0144'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
    ]

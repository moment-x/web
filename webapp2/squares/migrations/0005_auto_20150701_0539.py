# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squares', '0004_auto_20150701_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squares',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='squares',
            name='picture_entity',
        ),
        migrations.RemoveField(
            model_name='squares',
            name='text_entity',
        ),
        migrations.RemoveField(
            model_name='squares',
            name='web_entity',
        ),
        migrations.DeleteModel(
            name='Squares',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squares', '0002_auto_20150622_0725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squares',
            old_name='text_Entity',
            new_name='text_entity',
        ),
    ]

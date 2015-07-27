# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150627_0611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frdreq',
            old_name='guest',
            new_name='receiver',
        ),
        migrations.RenameField(
            model_name='frdreq',
            old_name='host',
            new_name='sender',
        ),
    ]

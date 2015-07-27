# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_users_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='avatar',
            new_name='Img',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='gender',
            new_name='cardNum',
        ),
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='sex',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

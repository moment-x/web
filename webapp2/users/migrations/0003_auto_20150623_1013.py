# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150622_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='users',
            name='day',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='month',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='year',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='identifier',
            field=models.CharField(unique=True, max_length=100, null=True),
        ),
    ]

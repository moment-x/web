# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('identifier', models.CharField(max_length=100, unique=True)),
                ('date_birth', models.DateField(null=True)),
                ('constellation', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

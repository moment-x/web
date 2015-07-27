# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squares',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('db_image', models.BinaryField(null=True)),
                ('tag', models.CharField(max_length=100, null=True)),
                ('symbol', models.CharField(max_length=100, null=True)),
                ('sr_image', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squares', '0005_auto_20150701_0539'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextEntityExtra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('idStr', models.CharField(null=True, max_length=100)),
                ('textId', models.CharField(null=True, max_length=100)),
                ('img', models.BinaryField(null=True)),
                ('local', models.CharField(null=True, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='textentity',
            name='addressArr',
        ),
        migrations.RemoveField(
            model_name='textentity',
            name='imgArr',
        ),
    ]

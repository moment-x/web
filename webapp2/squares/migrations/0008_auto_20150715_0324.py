# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squares', '0007_auto_20150709_0850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textentity',
            name='addressArr',
        ),
        migrations.RemoveField(
            model_name='textentity',
            name='imgArr',
        ),
        migrations.AddField(
            model_name='cards',
            name='first',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='textentity',
            name='time',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pictureentity',
            name='img',
            field=models.CharField(max_length=1048576, null=True),
        ),
        migrations.AlterField(
            model_name='textentity',
            name='coverImg',
            field=models.CharField(max_length=1048576, null=True),
        ),
        migrations.AlterField(
            model_name='textentity',
            name='titImg',
            field=models.CharField(max_length=1048576, null=True),
        ),
        migrations.AlterField(
            model_name='textentityextra',
            name='img',
            field=models.CharField(max_length=1048576, null=True),
        ),
        migrations.AlterField(
            model_name='webentity',
            name='coverImg',
            field=models.CharField(max_length=1048576, null=True),
        ),
    ]

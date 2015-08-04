# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAvatar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('url', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.RemoveField(
            model_name='users',
            name='Img',
        ),
        migrations.AddField(
            model_name='useravatar',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]

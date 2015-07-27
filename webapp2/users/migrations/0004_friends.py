# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150623_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('guest', models.ForeignKey(related_name='guest_friend', to=settings.AUTH_USER_MODEL)),
                ('host', models.ForeignKey(related_name='host_friend', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

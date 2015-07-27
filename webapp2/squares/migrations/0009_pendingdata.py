# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('squares', '0008_auto_20150715_0324'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingData',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('json', models.CharField(null=True, max_length=1048576)),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

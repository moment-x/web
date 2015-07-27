# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrdReq',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guest', models.ForeignKey(related_name='guest_frdreq', to=settings.AUTH_USER_MODEL)),
                ('host', models.ForeignKey(related_name='host_frdreq', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='friends',
            name='guest',
            field=models.ForeignKey(related_name='guest_frd', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friends',
            name='host',
            field=models.ForeignKey(related_name='host_frd', to=settings.AUTH_USER_MODEL),
        ),
    ]

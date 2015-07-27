# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('squares', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True)),
                ('image', models.BinaryField(null=True)),
                ('tag', models.CharField(max_length=100, null=True)),
                ('token_id', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PictureEntity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('image_path', models.CharField(max_length=100, null=True)),
                ('db_image', models.BinaryField(null=True)),
                ('token_id', models.CharField(max_length=100, null=True)),
                ('extra_text', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TextEntity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('image_path', models.CharField(max_length=100, null=True)),
                ('db_image', models.BinaryField(null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('text', models.CharField(max_length=1000, null=True)),
                ('picture', models.BinaryField(null=True)),
                ('position', models.BinaryField(null=True)),
                ('thumbnail', models.BinaryField(null=True)),
                ('token_id', models.CharField(max_length=100, null=True)),
                ('width', models.CharField(max_length=100, null=True)),
                ('height', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebEntity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('image_path', models.CharField(max_length=100, null=True)),
                ('url', models.CharField(max_length=100, null=True)),
                ('thumbnail', models.BinaryField(null=True)),
                ('token_id', models.CharField(max_length=100, null=True)),
                ('extra_text', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='squares',
            name='db_image',
        ),
        migrations.RemoveField(
            model_name='squares',
            name='sr_image',
        ),
        migrations.RemoveField(
            model_name='squares',
            name='symbol',
        ),
        migrations.RemoveField(
            model_name='squares',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='squares',
            name='title',
        ),
        migrations.AddField(
            model_name='squares',
            name='owner',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squares',
            name='picture_entity',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=1, related_name='square_of_picture'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squares',
            name='text_Entity',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=1, related_name='square_of_text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squares',
            name='web_entity',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=1, related_name='square_of_web'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='webentity',
            name='square',
            field=models.ForeignKey(to='squares.Squares'),
        ),
        migrations.AddField(
            model_name='textentity',
            name='square',
            field=models.ForeignKey(to='squares.Squares'),
        ),
        migrations.AddField(
            model_name='pictureentity',
            name='square',
            field=models.ForeignKey(to='squares.Squares'),
        ),
    ]

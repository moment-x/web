# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('squares', '0003_auto_20150624_0239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cards',
            old_name='tag',
            new_name='cardid',
        ),
        migrations.RenameField(
            model_name='cards',
            old_name='image',
            new_name='cardimg',
        ),
        migrations.RenameField(
            model_name='cards',
            old_name='title',
            new_name='cardtag',
        ),
        migrations.RenameField(
            model_name='cards',
            old_name='token_id',
            new_name='cardtitle',
        ),
        migrations.RenameField(
            model_name='pictureentity',
            old_name='db_image',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='pictureentity',
            old_name='extra_text',
            new_name='imgId',
        ),
        migrations.RenameField(
            model_name='pictureentity',
            old_name='image_path',
            new_name='imgText',
        ),
        migrations.RenameField(
            model_name='textentity',
            old_name='db_image',
            new_name='addressArr',
        ),
        migrations.RenameField(
            model_name='textentity',
            old_name='position',
            new_name='coverImg',
        ),
        migrations.RenameField(
            model_name='textentity',
            old_name='picture',
            new_name='imgArr',
        ),
        migrations.RenameField(
            model_name='textentity',
            old_name='image_path',
            new_name='textId',
        ),
        migrations.RenameField(
            model_name='textentity',
            old_name='thumbnail',
            new_name='titImg',
        ),
        migrations.RenameField(
            model_name='webentity',
            old_name='thumbnail',
            new_name='coverImg',
        ),
        migrations.RenameField(
            model_name='webentity',
            old_name='extra_text',
            new_name='pageId',
        ),
        migrations.RenameField(
            model_name='webentity',
            old_name='image_path',
            new_name='pageText',
        ),
        migrations.RenameField(
            model_name='webentity',
            old_name='token_id',
            new_name='urlStr',
        ),
        migrations.RemoveField(
            model_name='pictureentity',
            name='square',
        ),
        migrations.RemoveField(
            model_name='pictureentity',
            name='token_id',
        ),
        migrations.RemoveField(
            model_name='textentity',
            name='square',
        ),
        migrations.RemoveField(
            model_name='textentity',
            name='token_id',
        ),
        migrations.RemoveField(
            model_name='webentity',
            name='square',
        ),
        migrations.RemoveField(
            model_name='webentity',
            name='url',
        ),
        migrations.AddField(
            model_name='pictureentity',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='textentity',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='webentity',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='textentity',
            name='title',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]

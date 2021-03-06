# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 17:56
from __future__ import unicode_literals

import __main__
from django.db import migrations, models
import storagl.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=storagl.utils.short_uuid, unique=True)),
                ('file', models.FileField(storage=__main__.UploadStorage(), upload_to=storagl.utils.ShardedUpload(suffix_field='slug'))),
                ('file_name', models.CharField(blank=True, max_length=255)),
                ('content_type', models.CharField(blank=True, max_length=100)),
                ('last_access', models.DateTimeField(blank=True, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'assets',
            },
        ),
    ]

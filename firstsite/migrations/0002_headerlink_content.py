# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-26 05:24
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerlink',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=None),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-26 05:26
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstsite', '0002_headerlink_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerlink',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
    ]

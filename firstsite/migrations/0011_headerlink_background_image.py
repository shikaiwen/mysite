# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-13 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstsite', '0010_auto_20180226_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerlink',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/blog/uploads/header/%Y/%m/%d/'),
        ),
    ]

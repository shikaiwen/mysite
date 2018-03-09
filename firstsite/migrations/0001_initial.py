# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-26 05:20
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=100)),
                ('titletext', models.CharField(blank=True, max_length=100)),
                ('detailtext', models.CharField(blank=True, max_length=100)),
                ('show', models.BigIntegerField(blank=True, default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('meta_description', models.TextField(blank=True, max_length=160, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='static/blog/uploads/%Y/%m/%d/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
            ],
        ),
    ]
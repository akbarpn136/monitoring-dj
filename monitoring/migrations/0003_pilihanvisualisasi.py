# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 12:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0002_auto_20160223_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='PilihanVisualisasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=180, verbose_name='Nama Grafik')),
                ('info', models.CharField(max_length=200, verbose_name='Info Singkat')),
                ('deskripsi', models.TextField(verbose_name='Deskripsi Grafik')),
                ('thumb', models.TextField(validators=[django.core.validators.URLValidator()], verbose_name='Link Thumbnail')),
            ],
        ),
    ]

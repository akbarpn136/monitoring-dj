# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 16:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0007_auto_20170314_2220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dataangin',
            options={'ordering': ('tanggal',)},
        ),
    ]

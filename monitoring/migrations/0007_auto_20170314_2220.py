# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 15:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0006_pilihanvisualisasi_jenis'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dataangin',
            options={'ordering': ('-waktu',)},
        ),
    ]

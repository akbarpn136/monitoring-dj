# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-25 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0005_pilihanvisualisasi_daerah'),
    ]

    operations = [
        migrations.AddField(
            model_name='pilihanvisualisasi',
            name='jenis',
            field=models.CharField(choices=[('', '-----'), ('ATR', 'Atribut Angin'), ('PDF', 'Grafik PDF'), ('WRS', 'Grafik Windrose'), ('WTR', 'Grafik Waterfall'), ('RMS', 'Grafik RMS')], default='', max_length=3, verbose_name='Jenis Grafik'),
        ),
    ]

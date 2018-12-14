# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-12-14 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passerelle_imio_ts1_datasources', '0006_auto_20180301_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imiots1datasources',
            name='log_level',
        ),
        migrations.AlterField(
            model_name='destinationterm',
            name='slug',
            field=models.CharField(editable=False, max_length=100),
        ),
    ]
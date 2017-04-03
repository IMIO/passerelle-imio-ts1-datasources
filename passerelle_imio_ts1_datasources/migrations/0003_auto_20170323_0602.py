# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passerelle_imio_ts1_datasources', '0002_destinationterm'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinationterm',
            name='slug',
            field=models.CharField(default='slug', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='motivationterm',
            name='slug',
            field=models.CharField(default='slug', max_length=100),
            preserve_default=False,
        ),
    ]

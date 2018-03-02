# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passerelle_imio_ts1_datasources', '0005_auto_20180301_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motivationterm',
            name='slug',
            field=models.CharField(max_length=100, editable=False),
        ),
    ]

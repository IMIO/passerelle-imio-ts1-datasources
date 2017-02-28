# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passerelle_imio_ts1_datasources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationTerm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('description', models.TextField(max_length=500)),
                ('paymentrequired', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['text'],
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20151009_0326'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImioTs1Datasources',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('log_level', models.CharField(default=b'NOTSET', max_length=10, verbose_name='Log Level', choices=[(b'NOTSET', b'NOTSET'), (b'DEBUG', b'DEBUG'), (b'INFO', b'INFO'), (b'WARNING', b'WARNING'), (b'ERROR', b'ERROR'), (b'CRITICAL', b'CRITICAL'), (b'FATAL', b'FATAL')])),
                ('users', models.ManyToManyField(to='base.ApiUser', blank=True)),
            ],
            options={
                'verbose_name': 'TS1 datasources manage Service',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MotivationTerm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=4)),
                ('description', models.TextField(max_length=500)),
            ],
            options={
                'ordering': ['text'],
            },
            bases=(models.Model,),
        ),
    ]

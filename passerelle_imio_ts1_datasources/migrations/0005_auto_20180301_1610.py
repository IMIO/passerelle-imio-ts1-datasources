# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('passerelle_imio_ts1_datasources', '0004_auto_20180217_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imiots1datasources',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='imiots1datasources',
            name='log_level',
            field=models.CharField(default=b'INFO', max_length=10, verbose_name='Log Level', choices=[(b'NOTSET', b'NOTSET'), (b'DEBUG', b'DEBUG'), (b'INFO', b'INFO'), (b'WARNING', b'WARNING'), (b'ERROR', b'ERROR'), (b'CRITICAL', b'CRITICAL'), (b'FATAL', b'FATAL')]),
        ),
        migrations.AlterField(
            model_name='imiots1datasources',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='motivationterm',
            name='text',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex=b'^((?!,).)*$', message='Comma is not allowed in motivations title (NO ",").', code=b'invalid_text')]),
        ),
    ]

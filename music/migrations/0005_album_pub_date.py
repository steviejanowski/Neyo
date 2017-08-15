# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20170428_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]

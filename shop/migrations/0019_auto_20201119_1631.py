# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-19 13:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20201119_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 19, 16, 30, 59, 154398), verbose_name='Дата'),
        ),
    ]

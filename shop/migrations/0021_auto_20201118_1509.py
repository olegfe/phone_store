# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-18 12:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_auto_20201116_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 18, 15, 9, 9, 600856), verbose_name='Дата'),
        ),
    ]

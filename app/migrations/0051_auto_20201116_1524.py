# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-16 12:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0050_auto_20201116_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 16, 15, 24, 59, 621884), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 16, 15, 24, 59, 623882), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 16, 15, 24, 59, 624893), verbose_name='Дата'),
        ),
    ]

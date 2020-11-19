# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-19 15:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0064_auto_20201119_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 19, 18, 26, 25, 953439), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 19, 18, 26, 25, 953439), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 19, 18, 26, 25, 954436), verbose_name='Дата'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-19 10:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20201019_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 10, 19, 13, 22, 13, 302688), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 10, 19, 13, 22, 13, 302688), verbose_name='Дата'),
        ),
    ]

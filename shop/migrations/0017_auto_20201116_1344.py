# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-16 10:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='comment',
            field=models.CharField(max_length=5000, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 16, 13, 44, 39, 627595), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='minus',
            field=models.CharField(max_length=2000, verbose_name='Недоститки'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='plus',
            field=models.CharField(max_length=2000, verbose_name='Достоинства'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-13 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20201113_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cores',
            field=models.CharField(default=False, max_length=5, verbose_name='Кол-во ядер'),
        ),
        migrations.AlterField(
            model_name='product',
            name='display_type',
            field=models.CharField(default=False, max_length=10, verbose_name='Тип экрана'),
        ),
        migrations.AlterField(
            model_name='product',
            name='gpu',
            field=models.CharField(default=False, max_length=255, verbose_name='Графический ускроритель'),
        ),
        migrations.AlterField(
            model_name='product',
            name='processor',
            field=models.CharField(default=False, max_length=255, verbose_name='Процессор'),
        ),
        migrations.AlterField(
            model_name='product',
            name='resolution',
            field=models.CharField(default=False, max_length=20, verbose_name='Разрешение экрана'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-19 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_auto_20201119_1643'),
        ('orders', '0004_auto_20201119_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-18 12:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20201118_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='nickname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

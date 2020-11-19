# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-19 13:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20201119_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='nickname',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
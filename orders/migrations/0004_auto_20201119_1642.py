# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-19 13:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20201119_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='test',
        ),
        migrations.AlterField(
            model_name='order',
            name='nickname',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
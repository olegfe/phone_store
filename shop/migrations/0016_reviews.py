# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-16 10:42
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0015_auto_20201113_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plus', models.CharField(default=False, max_length=2000, verbose_name='Достоинства')),
                ('minus', models.CharField(default=False, max_length=2000, verbose_name='Недоститки')),
                ('comment', models.CharField(default=False, max_length=5000, verbose_name='Комментарий')),
                ('date', models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 16, 13, 42, 37, 214128), verbose_name='Дата')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзыв к продукту',
                'db_table': 'Отзывы',
                'ordering': ['-date'],
            },
        ),
    ]

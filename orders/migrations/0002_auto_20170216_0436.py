# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-16 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='телефон'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-16 10:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_discript'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='discript',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themenu', '0008_auto_20170114_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=96, unique=True),
        ),
    ]

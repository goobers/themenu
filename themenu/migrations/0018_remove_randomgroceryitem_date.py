# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-12 20:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('themenu', '0017_randomgroceryitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='randomgroceryitem',
            name='date',
        ),
    ]

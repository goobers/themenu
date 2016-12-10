# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 19:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('themenu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='meal',
        ),
        migrations.AddField(
            model_name='meal',
            name='menu',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='themenu.Menu'),
            preserve_default=False,
        ),
    ]

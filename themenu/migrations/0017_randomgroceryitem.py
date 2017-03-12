# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-12 18:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('themenu', '0016_auto_20170128_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='RandomGroceryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('date', models.DateField(verbose_name=b'random grocery item date')),
                ('purchased', models.BooleanField(default=False)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='themenu.Team')),
            ],
        ),
    ]

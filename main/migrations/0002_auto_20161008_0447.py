# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-07 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='update',
            name='update_time',
        ),
        migrations.AddField(
            model_name='update',
            name='index',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-21 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20170220_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='rmin',
            field=models.CharField(default=50, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='rsec',
            field=models.CharField(default=10, max_length=2, null=True),
        ),
    ]

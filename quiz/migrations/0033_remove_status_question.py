# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 12:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0032_auto_20170107_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='question',
        ),
    ]

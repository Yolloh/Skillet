# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-06 17:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0011_auto_20170906_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersubmission',
            name='verdict',
        ),
    ]
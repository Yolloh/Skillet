# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-30 07:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_fillstatus_userquestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fillstatus',
            name='userquestion',
        ),
        migrations.RemoveField(
            model_name='multistatus',
            name='userquestion',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-30 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='multistatus',
            name='userquestion',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
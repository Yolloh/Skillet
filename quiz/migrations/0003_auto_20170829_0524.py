# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-29 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='code',
            field=models.TextField(blank=True),
        ),
    ]

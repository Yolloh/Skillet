# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-06 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0005_auto_20170906_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='codequestionextend',
            name='constraint',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='codequestionextend',
            name='explanation',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='codequestionextend',
            name='input_statement',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='codequestionextend',
            name='output_statement',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]

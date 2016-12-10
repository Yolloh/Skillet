# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-10 19:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20161211_0007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]

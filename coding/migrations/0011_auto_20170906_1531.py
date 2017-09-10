# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-06 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0010_auto_20170906_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersubmission',
            old_name='remaining_time',
            new_name='rmin',
        ),
        migrations.RemoveField(
            model_name='usersubmission',
            name='wrong_line',
        ),
        migrations.AddField(
            model_name='usersubmission',
            name='expected_output',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usersubmission',
            name='failed_testcase',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usersubmission',
            name='ith_test_case_failed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usersubmission',
            name='rsec',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersubmission',
            name='verdict',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usersubmission',
            name='user_output',
            field=models.TextField(blank=True, null=True),
        ),
    ]
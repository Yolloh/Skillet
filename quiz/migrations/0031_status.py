# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 12:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0030_auto_20170107_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qstatus', models.CharField(choices=[(b'Red', b'Red'), (b'Yellow', b'Yellow'), (b'Green', b'Green')], default=b'Red', max_length=6)),
                ('selected', models.IntegerField(default=-1)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question', models.ManyToManyField(to='quiz.Question')),
            ],
        ),
    ]

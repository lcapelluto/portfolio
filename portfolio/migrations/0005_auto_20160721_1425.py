# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 14:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20160721_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='education',
            name='start_date',
        ),
        migrations.AddField(
            model_name='education',
            name='expected_graduation',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
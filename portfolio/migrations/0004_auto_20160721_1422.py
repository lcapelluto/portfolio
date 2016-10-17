# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 14:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20160721_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name_plural': 'education'},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name_plural': 'experience'},
        ),
        migrations.RemoveField(
            model_name='education',
            name='dates_attended',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='time_period',
        ),
        migrations.AddField(
            model_name='education',
            name='end_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='education',
            name='start_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='experience',
            name='end_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='experience',
            name='start_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]

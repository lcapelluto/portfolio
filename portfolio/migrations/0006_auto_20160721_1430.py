# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20160721_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='awards',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='education',
            name='clubs',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='education',
            name='major',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='education',
            name='societies',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]

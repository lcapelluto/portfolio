# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-27 08:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20160727_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direction',
            name='order',
        ),
    ]

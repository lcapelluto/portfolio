# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 14:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20160721_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='company_name',
            new_name='company',
        ),
    ]

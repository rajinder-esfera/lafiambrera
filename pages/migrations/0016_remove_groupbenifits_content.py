# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20170909_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupbenifits',
            name='content',
        ),
    ]

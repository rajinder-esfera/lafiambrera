# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-17 06:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carthandler', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='lunhbox',
        ),
    ]

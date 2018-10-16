# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-03 06:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0033_auto_20170703_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='u_processing_date_till',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 7, 10, 6, 58, 26, 355261, tzinfo=utc), null=True, verbose_name=b'Processing till date'),
        ),
    ]

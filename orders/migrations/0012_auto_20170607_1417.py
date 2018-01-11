# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 12:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20170518_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='u_processing_date_till',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 6, 14, 12, 17, 30, 249594, tzinfo=utc), null=True, verbose_name=b'Processing till date'),
        ),
    ]

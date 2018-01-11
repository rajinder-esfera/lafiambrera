# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 13:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0118_auto_20170812_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='u_processing_date_till',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 19, 13, 17, 21, 453874, tzinfo=utc), null=True, verbose_name='Processing till date'),
        ),
    ]
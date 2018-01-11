# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 10:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0162_auto_20170919_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='u_processing_date_till',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 9, 26, 10, 32, 26, 884887, tzinfo=utc), null=True, verbose_name='Processing till date'),
        ),
    ]

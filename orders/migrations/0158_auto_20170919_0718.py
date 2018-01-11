# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 05:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0157_auto_20170909_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='u_processing_date_till',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 9, 26, 5, 18, 17, 537866, tzinfo=utc), null=True, verbose_name='Processing till date'),
        ),
    ]
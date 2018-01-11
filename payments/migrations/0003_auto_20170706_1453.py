# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-06 12:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '0002_lafiambrera_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyToWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('lafiambera_credit', models.FloatField()),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_type',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='status',
        ),
    ]

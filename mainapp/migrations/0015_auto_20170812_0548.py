# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 03:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0014_invitrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='InviteRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uiid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.RemoveField(
            model_name='invitrequest',
            name='user',
        ),
        migrations.DeleteModel(
            name='InvitRequest',
        ),
    ]

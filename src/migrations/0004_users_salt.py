# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-31 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_auto_20190731_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='salt',
            field=models.CharField(default=b'', max_length=64),
        ),
    ]
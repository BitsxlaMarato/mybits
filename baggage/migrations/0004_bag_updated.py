# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-08-09 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baggage', '0003_auto_20180809_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='bag',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

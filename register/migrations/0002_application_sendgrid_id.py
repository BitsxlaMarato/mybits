# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_squashed_0005_fix_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='sendgrid_id',
            field=models.TextField(default=''),
        ),
    ]
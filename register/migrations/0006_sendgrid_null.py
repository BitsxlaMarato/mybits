# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-28 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_default_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='sendgrid_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
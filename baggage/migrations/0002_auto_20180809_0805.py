# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-08-09 06:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baggage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateField(auto_now_add=True)),
                ('comment', models.TextField(blank=True, max_length=1023, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='move',
            name='item',
        ),
        migrations.RemoveField(
            model_name='move',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='move',
            name='position',
        ),
        migrations.RemoveField(
            model_name='bag',
            name='active',
        ),
        migrations.AddField(
            model_name='bag',
            name='status',
            field=models.CharField(choices=[('LAPTOP', 'Laptop'), ('OTHER', 'Other')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='bag',
            name='time',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bag',
            name='type',
            field=models.CharField(choices=[('LAPTOP', 'Laptop'), ('OTHER', 'Other')], max_length=10),
        ),
        migrations.DeleteModel(
            name='Move',
        ),
        migrations.AddField(
            model_name='comment',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='baggage.Bag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-16 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]

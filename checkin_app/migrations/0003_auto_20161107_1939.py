# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin_app', '0002_auto_20161107_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
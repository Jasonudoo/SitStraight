# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-04 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posture', '0003_auto_20170104_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

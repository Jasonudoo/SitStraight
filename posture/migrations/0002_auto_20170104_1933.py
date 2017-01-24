# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-04 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posture', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_ip',
        ),
        migrations.AddField(
            model_name='user',
            name='user_eyeheight_baseline',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='user',
            name='user_eyeheight_current',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='user',
            name='user_photo_baseline',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='user_photo_current',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

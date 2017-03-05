# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-05 12:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_messages_ip'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'verbose_name': '留言', 'verbose_name_plural': '留言'},
        ),
        migrations.AlterField(
            model_name='messages',
            name='content',
            field=models.CharField(max_length=500, verbose_name='留言内容'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='time',
            field=django_unixdatetimefield.fields.UnixDateTimeField(default=datetime.datetime(2017, 3, 5, 20, 0, 56, 353779), verbose_name='留言时间'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 17:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dormdb', '0013_dorm_relay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dorm',
            name='relay1',
        ),
        migrations.RemoveField(
            model_name='dorm',
            name='relay2',
        ),
        migrations.RemoveField(
            model_name='dorm',
            name='relay3',
        ),
        migrations.RemoveField(
            model_name='dorm',
            name='relay4',
        ),
        migrations.RemoveField(
            model_name='dorm',
            name='relay5',
        ),
    ]

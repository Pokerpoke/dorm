# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dormdb', '0015_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='roomname',
            field=models.PositiveIntegerField(null=True),
        ),
    ]

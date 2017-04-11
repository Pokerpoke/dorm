# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dormdb', '0017_auto_20170410_1422'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]

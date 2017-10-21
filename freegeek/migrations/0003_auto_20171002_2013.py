# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freegeek', '0002_auto_20171002_2013'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='action',
            table='actions',
        ),
    ]

from __future__ import unicode_literals
from django.db import migrations


def load_stores_from_fixture(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "volunteer_task_type")


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0009_auto_20180115_0155'),
    ]

    operations = [
        migrations.RunPython(load_stores_from_fixture),
    ]

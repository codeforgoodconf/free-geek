from __future__ import unicode_literals
from django.db import migrations


def load_stores_from_fixture(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "weekdays")


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0010_seed_volunteer_task_types'),
    ]

    operations = [
        migrations.RunPython(load_stores_from_fixture),
    ]

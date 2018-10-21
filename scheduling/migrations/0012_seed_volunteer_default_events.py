from __future__ import unicode_literals
from django.db import migrations


def load_stores_from_fixture(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "volunteer_default_events")


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0011_seed_weekdays'),
    ]

    operations = [
        migrations.RunPython(load_stores_from_fixture),
    ]

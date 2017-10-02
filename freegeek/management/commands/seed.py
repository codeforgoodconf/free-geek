from django_seed import Seed
from django.core.management.base import BaseCommand

from freegeek.models import *

class Command(BaseCommand):
    def handle(self, **options):
        seeder = Seed.seeder()
        dummy = FGUser.objects.create(can_login=False, shared=False)

        seeder.add_entity(FGUser, 10, {
            'created_by': lambda x: dummy,
            'updated_by': lambda x: dummy,
        })
        seeder.add_entity(Contact, 10)
        seeder.add_entity(VolunteerDefaultEvent, 5)
        seeder.add_entity(VolunteerEvent, 5)
        seeder.add_entity(VolunteerTaskType, 5)
        seeder.add_entity(VolunteerDefaultShift, 5)
        seeder.add_entity(VolunteerShift, 5)

        inserted_pks = seeder.execute()

import unittest
from django.test import TestCase
from freegeek.models import Appointment
from freegeek.models import Station
from freekgeek.models import Location


class AppointmentTestCase(TestCase):
    def setUp(self):
        Appointment.objects.create(start_time = '2017-07-31 09:15', end_time = '2017-07-31 11:15', filled = False, proficiency= 'LEVEL1',  station = 'recycling')

    def test_appointment_str(self):
        """Testing that appointment string is returned with correct info and is grammatically correct"""
        appointment1 = Appointment.objects.get(start_time = '2017-07-31 09:15', end_time = '2017-07-31 11:15', filled = False, proficiency= 'LEVEL1',  station = 'recycling')
        self.assertEqual(appointment1.__str__(), 'Appointment: 2017-07-31 09:15 to 2017-07-31 11:15 at recycling in LOCATION requires L1')


class StationTestCase(TestCase):
    def setup(self):
        Station.objects.create()


class LocationTestCase(TestCase):
    def setup(self):
        Location.objects.create()
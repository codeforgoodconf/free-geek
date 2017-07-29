import unittest
from django.test import TestCase
from freegeek.models import Appointment
from freegeek.models import Station
from freekgeek.models import Location


class AppointmentTestCase(TestCase):
    def setUp(self):
        Appointment.objects.create()

    def test_appointment_str(self):
        """Testing that appointment string is returned with correct info and is grammatically correct"""


class StationTestCase(TestCase):
    def setup(self):
        Station.objects.create()


class LocationTestCase(TestCase):
    def setup(self):
        Location.objects.create()
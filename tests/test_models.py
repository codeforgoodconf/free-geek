import unittest
from django.test import TestCase
from freegeek.models import Appointment
from freegeek.models import Station
from freegeek.models import Location
from freegeek.models import create_location
from freegeek.models import create_station
from django.forms import ValidationError


class AppointmentTestCase(TestCase):
    """Test cases for Appointment
    """

    def test_create_appointment(self):
        """Testing that create_appointment creates an Appointment (and saves it in the database)
        """
        location1 = create_location(location_name = 'Location 1')
        station1 = create_station(station_name = 'Station 1', location_name = 'Location 1')
        appointment1 = Appointment.create_appointment(start_time = '2017-07-31 09:15-0800', end_time = '2017-07-31 11:15-0800', proficiency = 'Skill 1', station_name = 'Station 1', location_name = 'Location 1')
        appointment = Appointment.objects.get(start_time = '2017-07-31 09:15-0800', end_time = '2017-07-31 11:15-0800', proficiency = 'Skill 1', station__name = 'Station 1', station__location__name = 'Location 1')
        num_appointment_objects = Appointment.objects.filter(start_time = '2017-07-31 09:15-0800', end_time = '2017-07-31 11:15-0800', proficiency = 'Skill 1', station__name = 'Station 1', station__location__name = 'Location 1').count()
        self.assertEqual(num_appointment_objects, 1)


class StationTestCase(TestCase):
    """Test cases for Station
    """

    def test_create_station_succeeds_when_location_exists(self):
        """Test that create_station creates a Station when there is a unique Location with name=location_name
        """
        location1 = create_location(location_name = 'Location 1')
        station1 = create_station(station_name = 'Station 1', location_name = 'Location 1')
        num_station_objects = Station.objects.filter(name = 'Station 1', location__name = 'Location 1').count()
        station = Station.objects.get(name = 'Station 1', location__name = 'Location 1')
        self.assertEqual(station.__str__(), 'Station 1')
        self.assertEqual(num_station_objects, 1)

    def test_create_station_fails_when_location_does_not_exist(self):
        """Test that create_station will not create a Station if there is no Location with name=location_name
        """
        try:
            station1 = create_station(station_name = 'Station 1', location_name = 'Location 1')
        except ValidationError:
            pass
        num_station_objects = Station.objects.filter(name = 'Station 1', location__name = 'Location 1').count()
        self.assertEqual(num_station_objects, 0)

    def test_create_station_fails_when_station_already_exists(self):
        """Test that create_station will not create a new Station if a Station with name=station_name already exists at the Location with name=location_name
        """
        location1 = create_location(location_name = 'Location 1')
        station1 = create_station(station_name = 'Station 1', location_name = 'Location 1')
        try:
            station1 = create_station(station_name = 'Station 1', location_name = 'Location 1')
        except ValidationError:
            pass
        num_station_objects = Station.objects.filter(name = 'Station 1', location__name = 'Location 1').count()
        self.assertEqual(num_station_objects, 1)
        
    def test_create_station_can_add_second_station_to_location(self):
        """Test that create_station can add two Stations with unique names to a single Location
        """
        location1 = create_location(location_name = 'Location 1')
        station1 = create_station(station_name = 'Station 1', location_name = 'Location 1')
        try:
            station2 = create_station(station_name = 'Station 2', location_name = 'Location 1')
        except ValidationError:
            pass
        num_station_objects = Station.objects.filter(location__name = 'Location 1').count()
        self.assertEqual(num_station_objects, 2)
        

class LocationTestCase(TestCase):
    """Test cases for Location
    """

    def test_create_location(self):
        """Test that create_location can create a Location
        """
        location1 = create_location(location_name = 'Location 1')
        num_location_objects = Location.objects.filter(name = 'Location 1').count()
        location = Location.objects.get(name = 'Location 1')
        self.assertEqual(location1.__str__(), 'Location 1')
        self.assertEqual(num_location_objects, 1)

    def test_create_location_fails_when_location_already_exists(self):
        """Test that create_location will not create a new Location if a Location with the same name already exists
        """
        location1 = create_location(location_name = 'Location 1')
        try:
            location1 = create_location(location_name = 'Location 1')
        except ValidationError:
            pass
        num_location_objects = Location.objects.filter(name = 'Location 1').count()
        self.assertEqual(num_location_objects, 1)
        


# To run tests run python manage.py test tests to run all || python manage.py test tests test_models to just run this file


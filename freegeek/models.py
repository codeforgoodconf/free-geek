import datetime

from django.db import models
from django.utils import timezone


class Building(models.Model):
    """Building model.
    
    (There are multiple FreeGeek locations.)
    """
    building_name = models.CharField(max_length=200)
    def __str__(self):
        return self.building_name

class Station(models.Model):
    """Station model.
    
    Has a station_name.
    Associated with a Building. (Where the Station is located.)
    """
    station_name = models.CharField(max_length=200)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    def __str__(self):
        return self.station_name

class Appointment(models.Model):
    """Appointment model.

    Attributes:
       start_time (DateTimeField)
       end_time (DateTimeField)
       station (ForeignKey(Station))

    It needs "slots" which have proficiency requirements, 
    and each slot can be open or filled.
    (Do we need a "slot" model?)
    """
    start_time = models.DateTimeField('start_time')
    end_time = models.DateTimeField('end_time')
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    def __str__(self):
        """Recast Appointment as string which gives a summary of the Appointment.
        This includes start_time, end_time, station, and location.
        This should eventually include a summary of open and filled slots.
        """
        appointment_string = ("Appointment: %s to %s at %s in %s" % 
                              (str(self.start_time), str(self.end_time), 
                               str(self.station), str(self.station.building)))
        return appointment_string


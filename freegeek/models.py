import datetime

from django.db import models
from django.utils import timezone


# Create your models here.                                                                                                                                               
class Appointment(models.Model):
    start_time = models.DateTimeField('start_time')
    end_time = models.DateTimeField('start_time')
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    def __str__(self):
        appointment_string = "Appointment: %s to %s at %s in %s" % (str(self.start_time), str(self.end_time), str(self.station), str(self.station.factory))
        return appointment_string

class Station(models.Model):
    station_name = models.CharField(max_length=200)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    def __str__(self):
        return self.station_name

class Factory(models.Model):
    factory_name = models.CharField(max_length=200)
    def __str__(self):
        return self.factory_name


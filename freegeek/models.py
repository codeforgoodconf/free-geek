from django.db import models
from django.contrib import admin
import datetime
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import User, UserManager
from django.forms import ValidationError
from . import settings

DURATION_ZERO = datetime.time(hour=0)
DEFAULT_DURATION = datetime.time(hour=1)
DEFAULT_TIME = datetime.time(hour=12)

phoneValidator = RegexValidator(
    regex=r'[0-9][0-9 ]+',
    message='Not a valid phone number')


class Staff(UserManager)

    """ Staff details.

    Staff can add Volunteers.
    Staff can turn Volunteers into Interns.
    Staff can add Teachers.
    Staff can turn Volunteers and Interns into Teachers.
    """

    def get_by_natural_key(self, username):
        """                                                                                                                                                              
        Enable serialisation without pk. Not needed ATM.                                                                                                                 
        """
    return self.get(username=username)


    def create_user(self,
        username,
        first_name,
        last_name,
        email,
        phone,
        date_of_birth,
        gender,
        notes,
        password=None
    ):
        """                                                                                                                                                              
        Creates and saves a User with the given particulars and password.                                                                                            
        """
        if not username:
            raise ValueError('User must have a username')

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            date_of_birth=date_of_birth,
            gender=gender,
            notes=notes,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class Volunteer(User):
    """ Volunteer details.

    Volunteer can (un)schedule self for appointment.
    """

    # gender options                                                                                                                                                     
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    # title options                                                                                                                                                      
    MR = 'MR'
    MRS = 'MRS'
    MISS = 'MISS'
    MS = 'MS'
    DR = 'DR'
    PROF = 'PROF'
    REV = 'REV'
    TITLE_CHOICES = (
        (MR, 'Mr'),
        (MRS, 'Mrs'),
        (MISS, 'Miss'),
        (MS, 'Ms'),
        (DR, 'Dr'),
        (PROF, 'Prof'),
        (REV, 'Rev'),
    )

    class Meta(User.Meta):
        verbose_name = 'Volunteer'
        verbose_name_plural = 'Volunteers'
        
    objects = Staff()

    title = models.CharField(
        max_length=4,
        choices=TITLE_CHOICES,
        default=MRS,
    )
    phone = models.CharField(
        max_length=20,
        validators=[phoneValidator],
        blank=True,
        null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=FEMALE,
    )
    notes = models.TextField(blank=True)


    def natural_key(self):
        """                                                                                                                                                              
        Serialisation aid. Not needed ATM.                                                                                                                               
        """
        return (self.username,)


    def age(self):
        """                                                                                                                                                              
        Age to the nearest year.                                                                                                                                         
        """
        if self.date_of_birth:
            now = timezone.now()
            return now.year - self.date_of_birth.year
        return None


    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)



class Intern(Volunteer):
    """Intern details.

    Intern is a Volunteer with additional priveleges:
    Intern can (un)schedule Volunteers in own Crew for appointment.
    """

    class Meta(User.Meta):
        verbose_name = 'Intern'
        verbose_name_plural = 'Interns'



class Teacher(Volunteer):
    """Teacher details.

    Teacher is a Volunteer with additional priveleges:
    Teacher can (un)schedule Volunteers in any Crew for appointment.
    """

    class Meta(User.Meta):
        verbose_name = 'Volunteer'
        verbose_name_plural = 'Volunteers'




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


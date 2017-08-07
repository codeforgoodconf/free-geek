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

#from models_old import *

class ProfileManager(UserManager):
    """ only users with the staff level can add and modify Profiles """
    
    def get_by_natural_key(self, username):
        """
        Enable serialisation without pk. Not needed ATM.
        """
        return self.get(username=username)

    def create_user(self,
                    username,
                    first_name,
                    last_name,
                    proficiency,
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

        user = Profile(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            phone=phone,
            date_of_birth=date_of_birth,
            gender=gender,
            proficiency=proficiency,
            notes=notes,
            password=password,
        )

        user.set_password(password)
        #user.save(using=self._db)
        user.save()
        return user


class Profile(User):
    """ Profile details.

    Attributes:
       Proficiency level
       IsVolunteer (bool)
       IsIntern (bool)
       IsTeacher (bool)

    Profile can (un)schedule self for appointment.

    Need to be able to see all scheduled appointments for the profile.
    """

    IsVolunteer = True
    IsIntern = False
    IsTeacher = False

    # proficiency options
    LEVEL1 = 'L1'
    LEVEL2 = 'L2'
    LEVEL3 = 'L3'
    LEVEL_CHOICES = (
        (LEVEL1, 'Level 1'),
        (LEVEL2, 'Level 2'),
        (LEVEL3, 'Level 3'),
    )

    # gender options
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )

    # title options
    # MAKE SURE TO HANDLE THE "NONE" OPTION FOR OUTPUT CORRECTLY.

    MR = 'MR'
    MRS = 'MRS'
    MISS = 'MISS'
    MS = 'MS'
    DR = 'DR'
    PROF = 'PROF'
    REV = 'REV'
    NOTITLE = 'NONE'
    TITLE_CHOICES = (
        (MR, 'Mr'),
        (MRS, 'Mrs'),
        (MISS, 'Miss'),
        (MS, 'Ms'),
        (DR, 'Dr'),
        (PROF, 'Prof'),
        (REV, 'Rev'),
        (NOTITLE, 'None'),
    )

    class Meta(User.Meta):
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    objects = ProfileManager()

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
    proficiency = models.CharField(
        max_length=40,
        choices=LEVEL_CHOICES,
        default=LEVEL1,
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


class Location(models.Model):
    """Location model.

    (There are multiple FreeGeek locations.)
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

def create_location(location_name):
    """Create a location.
    
    Check that location does not already exist.
    """
    if not location_name:
        raise ValueError('Location must have a name.')
    num_location_objects = Location.objects.filter(name=location_name).count()
    if(num_location_objects >= 1):
        validation_error_string = ("%s instances of Location with name %s were found, require 0." % (str(num_location_objects), location_name))
        raise ValidationError(validation_error_string)
    
    location = Location(
        name=location_name,
        )
    location.save()
    return location
    

class Station(models.Model):
    """Station model.

    Has a station_name.
    Associated with a Location. (Where the Station is located.)
    """
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
def create_station(station_name, location_name):
    """Create a station.
    
    Check that location with name==location already exists.
    Check that station with name==name and location.name==location does not already exist.
    """
    
    if not station_name:
        raise ValueError('Station must have a name.')
    if not location_name:
        raise ValueError('Station must have a location.')
    
    num_location_objects = Location.objects.filter(name=location_name).count()
    if(num_location_objects != 1):
        validation_error_string = ("%s instances of location with name %s were found, require 1." % (str(num_location_objects), location_name))
        raise ValidationError(validation_error_string)
    
    num_station_objects = Station.objects.filter(name=station_name,location__name=location_name).count()
    if(num_station_objects >= 1):
        validation_error_string = ("%s instances of station with name %s were found, require 0." % (str(num_station_objects), station_name))
        raise ValidationError(validation_error_string)
    
    station = Station(
        name=station_name,
        location=Location.objects.get(name=location_name),
        )
    station.save()
    return station
        

class Appointment(models.Model):
    """Appointment model.

    Attributes:
       start_time (DateTimeField)
       end_time (DateTimeField)
       proficiency (str)
       station (ForeignKey(Station))
       filled
       profile
    """
    start_time = models.DateTimeField('start_time')
    end_time = models.DateTimeField('end_time')
    filled = models.BooleanField('filled')
    # NOT SURE THIS IS THE RIGHT WAY TO HANDLE THE PROFILE ASSIGNED TO THE APPOINTMENT
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, blank=True, null=True)

    # proficiency options
    LEVEL1 = 'L1'
    LEVEL2 = 'L2'
    LEVEL3 = 'L3'
    LEVEL_CHOICES = (
        (LEVEL1, 'Level 1'),
        (LEVEL2, 'Level 2'),
        (LEVEL3, 'Level 3'),
    )

    proficiency = models.CharField(
        max_length=40,
        choices=LEVEL_CHOICES,
        default=LEVEL1,
    )

    station = models.ForeignKey(Station, on_delete=models.CASCADE)

    # Do not check here whether they have same Station
    # This can be done separately (e.g. when iterating through all appointments)
    def __eq__(self, other):
        """Determine if Appointments overlap
        NOTE: time period end time is non-inclusive.
        """
        if (self.end_time <= other.start_time):
            return False
        if (self.start_time >= other.end_time):
            return False
        return True

    def __str__(self):
        """Recast Appointment as string which gives a summary of the Appointment.
        This includes start_time, end_time, station, location, and proficiency.
        """
        filled_string = 'unfilled'
        if self.filled:
            filled_string = 'filled by %s %s' % (self.profile.first_name, self.profile.last_name)
        appointment_string = ("From %s to %s at %s in %s requires proficiency %s, currently %s." % 
                              (str(self.start_time), str(self.end_time), 
                               str(self.station), str(self.station.location),
                               self.proficiency, filled_string))
        return appointment_string


    def create_appointment(start_time, end_time, station_name, location_name, proficiency):
        """Create an appointment
        
        Would be nice to check whether the appointment is at the same time as other
        appointments, and confirm whether overlapping appointments are intentional.
        
        Creating multiple appointments with a single action would be nice, but
        that will probably be taken care of in views.
        """
        if not start_time:
            raise ValueError('Appointment must have a start_time.')
        if not end_time:
            raise ValueError('Appointment must have an end_time.')
        if not station_name:
            raise ValueError('Appointment must have a station_name.')
        if not location_name:
            raise ValueError('Appointment must have a location_name.')
        if not proficiency:
            raise ValueError('Appointment must have a proficiency.')
        
        if (start_time > end_time):
            raise ValidationError('Start time must come before end time.')
        
        num_station_objects = Station.objects.filter(name=station_name,location__name=location_name).count()
        if(num_station_objects != 1):
            validation_error_string = ("%s instances of station with name %s, location %s, were found, require 1." % 
                                       (str(num_station_objects), station_name, location_name))
            raise ValidationError(validation_error_string)
        
        appointment = Appointment(
            start_time=start_time,
            end_time=end_time,
            station=Station.objects.get(name=station_name,location__name=location_name),
            proficiency=proficiency,
            filled=False,
            profile=None,
            )
        appointment.save()
        return appointment
    

# This could be a member function of Appointment and/or Profile instead
def assign_profile_to_appointment(profile, appointment):
    """Assign a profile to an appointment.

    Need to check that appointment is not already filled.
    Need to check that profile has the correct proficiency level.
    """

    if (appointment.filled):
        raise ValidationError(
            'Appointment is already filled.'
            )
        return False
    if(appointment.proficiency!=profile.proficiency):
        raise ValidationError(
            'Profile does not have appropriate proficiency level.'
            )
        return False

    appointment.filled = True
    appointment.profile = profile
    appointment.save()
    return True


# This could be a member function of Appointment instead
def unassign_appointment(appointment):
    """Unassign a profile from an appointment.

    Need to check that appointment is filled.
    """

    if (not appointment.filled):
        raise ValidationError(
            'Appointment is not yet filled.'
            )
        return False

    appointment.filled = False
    appointment.profile = None
    appointment.save()
    return True

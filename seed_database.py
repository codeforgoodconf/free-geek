from freegeek.models import Appointment, Station, Location, Profile, ProfileManager
from freegeek.models import assign_profile_to_appointment
from freegeek.models import unassign_appointment
from freegeek.models import create_station, create_location
from django.utils import timezone
import datetime 

l0 = Location(name='NorthSide')
l0.save()

l1 = Location(name='WestSide')
l1.save()

s0 = l0.station_set.create(name='Administration')
s0.save()

s1 = l0.station_set.create(name='Recycling')
s1.save()

s2 = l0.station_set.create(name='Building')
s2.save()

s3 = l0.station_set.create(name='Education')
s3.save()

s4 = l1.station_set.create(name='Recycling')
s4.save()

s5 = l1.station_set.create(name='Building')
s5.save()

a0 = s1.appointment_set.create(start_time=timezone.now()+datetime.timedelta(days=7),\
end_time=timezone.now()+datetime.timedelta(days=7,hours=1),\
proficiency='L1',filled=False,profile=None)
a0.save()

a1 = s1.appointment_set.create(start_time=timezone.now()+datetime.timedelta(days=6),\
end_time=timezone.now()+datetime.timedelta(days=6,hours=1),\
proficiency='L2',filled=False,profile=None)
a1.save()

a2 = s2.appointment_set.create(start_time=timezone.now()+datetime.timedelta(days=5),\
end_time=timezone.now()+datetime.timedelta(days=5,hours=1),\
proficiency='L3',filled=False,profile=None)
a2.save()

a3 = s2.appointment_set.create(start_time=timezone.now()+datetime.timedelta(days=4),\
end_time=timezone.now()+datetime.timedelta(days=4,hours=1),\
proficiency='L3',filled=False,profile=None)
a2.save()

pm = ProfileManager
p0=pm.create_user(pm,'jimmyj','Jimmy','Jimmereeno','L1','jimmyj@gmail.com','(123)456-7890','1988-8-18','M','')
p1=pm.create_user(pm,'mickeym','Mickey','Mickeranno','L2','mickym@gmail.com','(233)232-3223','2003-3-22','F','')
p2=pm.create_user(pm,'paulyp','Pauley','Paulerono','L3','paulyp@gmail.com','(505)555-5050','1995-5-15','O','')


assign_profile_to_appointment(p0,a0)
assign_profile_to_appointment(p1,a1)
assign_profile_to_appointment(p2,a2)


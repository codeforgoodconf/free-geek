from django.contrib import admin
from .models import *

admin.site.register(VolunteerTaskType)
admin.site.register(VolunteerTask)
admin.site.register(VolunteerDefaultEvent)
admin.site.register(VolunteerEvent)
admin.site.register(VolunteerDefaultShift)
admin.site.register(VolunteerShift)
admin.site.register(Assignment)
from django.contrib import admin
from .models import VolunteerTaskType # VolunteerTask, VolunteerDefaultEvent, VolunteerEvent

admin.site.register(VolunteerTaskType)
# admin.site.register(VolunteerTask)
# admin.site.register(VolunteerDefaultEvent)
# admin.site.register(VolunteerEvent)
from django.contrib import admin
from .models import Program, Contact, Roster, VolunteerTask, VolunteerTaskType, VolunteerDefaultEvent, VolunteerEvent


admin.site.register(Program)
admin.site.register(Contact)
admin.site.register(Roster)
admin.site.register(VolunteerTaskType)
admin.site.register(VolunteerTask)
admin.site.register(VolunteerDefaultEvent)
admin.site.register(VolunteerEvent)
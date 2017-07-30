from django.contrib import admin
from .models import Shift, Worker, Role, Profile


class ShiftAdmin(admin.ModelAdmin):
    pass


class WorkerAdmin(admin.ModelAdmin):
    pass


class RoleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Shift, ShiftAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Profile)

# Users
# Shifts
# Weekdays
# Workers
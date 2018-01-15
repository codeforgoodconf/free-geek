from django.db import models
from django.contrib.auth.models import User
from freegeek.models import Program, Contact, Roster


class VolunteerTaskType(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100, blank=True, null=True)
    hours_multiplier = models.DecimalField(max_digits=10, decimal_places=3)
    instantiable = models.BooleanField()
    lock_version = models.IntegerField()
    effective_on = models.DateTimeField(blank=True, null=True)
    ineffective_on = models.DateTimeField(blank=True, null=True)
    adoption_credit = models.NullBooleanField()

    program = models.ForeignKey(Program, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'volunteer_task_types'


class VolunteerTask(models.Model):
    duration = models.FloatField(blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    date_performed = models.DateField(blank=True, null=True)

    contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING)
    program = models.ForeignKey(Program, on_delete=models.DO_NOTHING)
    volunteer_task_type = models.ForeignKey(VolunteerTaskType, on_delete=models.DO_NOTHING)
    community_service_type = models.ForeignKey('CommunityServiceType', blank=True, null=True, on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(User, related_name='updated_by_user', on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, related_name='created_by_user', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'volunteer_tasks'


class VolunteerDefaultEvent(models.Model):
    week = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    weekday = models.ForeignKey('Weekday', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'volunteer_default_events'


class VolunteerEvent(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    nowalkins = models.BooleanField()

    volunteer_default_event = models.ForeignKey(VolunteerDefaultEvent, blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'volunteer_events'


class VolunteerDefaultShift(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    slot_count = models.IntegerField(blank=True, null=True)
    class_credit = models.NullBooleanField()
    not_numbered = models.BooleanField()
    stuck_to_assignment = models.BooleanField()

    effective_on = models.DateField(blank=True, null=True)
    ineffective_on = models.DateField(blank=True, null=True)

    program = models.ForeignKey(Program, on_delete=models.DO_NOTHING)
    roster = models.ForeignKey(Roster, on_delete=models.DO_NOTHING)
    volunteer_task_type = models.ForeignKey(VolunteerTaskType, null=True, on_delete=models.DO_NOTHING)
    volunteer_default_event = models.ForeignKey(VolunteerDefaultEvent, blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'volunteer_default_shifts'


class VolunteerShift(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    slot_number = models.IntegerField(blank=True, null=True)
    class_credit = models.NullBooleanField()
    not_numbered = models.BooleanField()
    stuck_to_assignment = models.BooleanField()

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    program = models.ForeignKey(Program, on_delete=models.DO_NOTHING)
    roster = models.ForeignKey(Roster, on_delete=models.DO_NOTHING)
    volunteer_task_type = models.ForeignKey(VolunteerTaskType, blank=True, null=True, on_delete=models.DO_NOTHING)
    volunteer_event = models.ForeignKey(VolunteerEvent, on_delete=models.DO_NOTHING)
    volunteer_default_shift = models.ForeignKey(VolunteerDefaultShift, blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'volunteer_shifts'


class Assignment(models.Model):
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    closed = models.BooleanField()
    lock_version = models.IntegerField()

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING)
    volunteer_shift = models.ForeignKey(VolunteerShift, on_delete=models.DO_NOTHING)
    call_status_type = models.ForeignKey('CallStatusType', blank=True, null=True, on_delete=models.DO_NOTHING)
    attendance_type = models.ForeignKey('AttendanceType', blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'assignments'


class AttendanceType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    cancelled = models.NullBooleanField()

    class Meta:
        db_table = 'attendance_types'


class CallStatusType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'call_status_types'


class Weekday(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    is_open = models.NullBooleanField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    open_time = models.TimeField()
    close_time = models.TimeField()

    class Meta:
        db_table = 'weekdays'


class CommunityServiceType(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100, blank=True, null=True)
    hours_multiplier = models.FloatField()
    lock_version = models.IntegerField()

    class Meta:
        db_table = 'community_service_types'
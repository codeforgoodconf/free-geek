from django.db import models
from django.contrib.auth.models import User
from freegeek.models import Program, Roster


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
    contact_id = models.IntegerField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    date_performed = models.DateField(blank=True, null=True)

    community_service_type_id = models.IntegerField(blank=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.DO_NOTHING)
    volunteer_task_type = models.ForeignKey(VolunteerTaskType, on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(User, related_name='updated_by_user', on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, related_name='created_by_user', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'volunteer_tasks'


class VolunteerDefaultEvent(models.Model):
    week = models.CharField(max_length=1, blank=True, null=True)
    weekday_id = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

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
    roster = models.ForeignKey(Roster, blank=True, null=True, on_delete=models.DO_NOTHING)
    volunteer_task_type = models.ForeignKey(VolunteerTaskType, null=True, on_delete=models.DO_NOTHING)
    volunteer_default_event = models.ForeignKey(VolunteerDefaultEvent, blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'volunteer_default_shifts'
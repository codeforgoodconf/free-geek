from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    is_organization = models.NullBooleanField()
    sort_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    middle_name = models.CharField(max_length=25, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    extra_address = models.CharField(max_length=52, blank=True, null=True)
    address = models.CharField(max_length=52, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state_or_province = models.CharField(max_length=15, blank=True, null=True)
    postal_code = models.CharField(max_length=25, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    lock_version = models.IntegerField()
    next_milestone = models.IntegerField(blank=True, null=True)
    contract_id = models.IntegerField()
    fully_covered = models.NullBooleanField()
    birthday = models.DateField(blank=True, null=True)
    volunteer_intern_title = models.CharField(max_length=255, blank=True, null=True)
    next_monthly_milestone = models.IntegerField(blank=True, null=True)
    exported_to_sf = models.DateTimeField(blank=True, null=True)
    household = models.IntegerField(blank=True, null=True)
    addr_rejected = models.NullBooleanField()
    addr_certified = models.BooleanField()

    class Meta:
        db_table = 'contacts'


class Program(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    volunteer = models.BooleanField()
    adoption_credit = models.BooleanField()

    def __str__(self):
        return self.description if self.description else self.name

    class Meta:
        db_table = 'programs'


class Roster(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    enabled = models.BooleanField()
    limit_shift_signup_by_program = models.BooleanField()
    contact_type_id = models.IntegerField(blank=True, null=True)
    restrict_to_every_n_days = models.IntegerField(blank=True, null=True)
    restrict_from_sked_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name if self.name else "[no name provided]"

    class Meta:
        db_table = 'rosters'
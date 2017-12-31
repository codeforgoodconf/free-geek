# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Action(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('FGUser', db_column='created_by', related_name='created_actions_set')
    updated_by = models.ForeignKey('FGUser', db_column='updated_by', related_name='updated_actions_set')
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'actions'


class Assignment(models.Model):
    volunteer_shift = models.ForeignKey('VolunteerShift', blank=True, null=True)
    contact_id = models.IntegerField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    attendance_type_id = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    call_status_type_id = models.IntegerField(blank=True, null=True)
    closed = models.BooleanField()
    lock_version = models.IntegerField()

    class Meta:
        db_table = 'assignments'


class AttendanceType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    cancelled = models.NullBooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'attendance_types'


class BuilderTask(models.Model):
    cashier_signed_off_by = models.ForeignKey('FGUser', db_column='cashier_signed_off_by', blank=True, null=True)
    action_id = models.IntegerField()
    contact_id = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'builder_tasks'


class CallStatusType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'call_status_types'


class CommunityServiceType(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)
    hours_multiplier = models.FloatField()
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'community_service_types'


class ContactDuplicate(models.Model):
    contact_id = models.IntegerField()
    dup_check = models.TextField()

    class Meta:
        db_table = 'contact_duplicates'


class ContactMethodType(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'contact_method_types'


class ContactMethod(models.Model):
    contact_method_type_id = models.IntegerField()
    value = models.CharField(max_length=100)
    ok = models.NullBooleanField()
    contact_id = models.IntegerField(blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    details = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'contact_methods'


class ContactType(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)
    for_who = models.CharField(max_length=3, blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    instantiable = models.BooleanField()
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'contact_types'


class ContactTypesContact(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contact_id = models.IntegerField()
    contact_type_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'contact_types_contacts'


class ContactVolunteerTaskTypeCount(models.Model):
    contact_id = models.IntegerField(blank=True, null=True)
    volunteer_task_type_id = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'contact_volunteer_task_type_counts'


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
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('FGUser', db_column='created_by', related_name='created_by_contacts_set')
    updated_by = models.ForeignKey('FGUser', db_column='updated_by', related_name='updated_by_contacts_set', blank=True, null=True)
    next_milestone = models.IntegerField(blank=True, null=True)
    addr_certified = models.BooleanField()
    contract_id = models.IntegerField()
    cashier_created_by = models.ForeignKey('FGUser', db_column='cashier_created_by',
        related_name='cashier_created_contacts_set',
        blank=True, null=True)
    cashier_updated_by = models.ForeignKey('FGUser', db_column='cashier_updated_by',
        related_name='cashier_updated_contacts_set',
        blank=True, null=True)
    fully_covered = models.NullBooleanField()
    birthday = models.DateField(blank=True, null=True)
    volunteer_intern_title = models.CharField(max_length=255, blank=True, null=True)
    next_monthly_milestone = models.IntegerField(blank=True, null=True)
    exported_to_sf = models.DateTimeField(blank=True, null=True)
    household = models.IntegerField(blank=True, null=True)
    addr_rejected = models.NullBooleanField()

    class Meta:
        db_table = 'contacts'


class ContactsMailing(models.Model):
    contact_id = models.IntegerField(blank=True, null=True)
    mailing_id = models.IntegerField()
    bounced = models.BooleanField()
    response_date = models.DateTimeField(blank=True, null=True)
    response_amount_cents = models.IntegerField(blank=True, null=True)
    response_note = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'contacts_mailings'


class Contract(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    instantiable = models.BooleanField()

    class Meta:
        db_table = 'contracts'


class Customization(models.Model):
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'customizations'


class DefaultAssignment(models.Model):
    contact_id = models.IntegerField(blank=True, null=True)
    volunteer_default_shift = models.ForeignKey('VolunteerDefaultShift', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    slot_number = models.IntegerField(blank=True, null=True)
    closed = models.BooleanField()
    week = models.CharField(max_length=1, blank=True, null=True)
    week_1_of_month = models.BooleanField()
    week_2_of_month = models.BooleanField()
    week_3_of_month = models.BooleanField()
    week_4_of_month = models.BooleanField()
    week_5_of_month = models.BooleanField()
    lock_version = models.IntegerField()

    class Meta:
        db_table = 'default_assignments'


class Default(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'defaults'


class DisbursementType(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'disbursement_types'


class Disbursement(models.Model):
    comments = models.TextField(blank=True, null=True)
    contact_id = models.IntegerField()
    disbursement_type_id = models.IntegerField()
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    disbursed_at = models.DateTimeField()
    needs_attention = models.BooleanField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    cashier_created_by = models.ForeignKey('FGUser', db_column='cashier_created_by',
        related_name='cashier_created_by_disbursements_set',
        blank=True, null=True)
    cashier_updated_by = models.ForeignKey('FGUser', db_column='cashier_updated_by',
        related_name='cashier_updated_by_disbursements_set',
        blank=True, null=True)
    adjustment = models.BooleanField()

    class Meta:
        db_table = 'disbursements'


class DisciplinaryActionArea(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'disciplinary_action_areas'


class DisciplinaryActionAreasDisciplinaryAction(models.Model):
    disciplinary_action_id = models.IntegerField(blank=True, null=True)
    disciplinary_action_area_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'disciplinary_action_areas_disciplinary_actions'


class DisciplinaryAction(models.Model):
    notes = models.TextField(blank=True, null=True)
    contact_id = models.IntegerField()
    disabled = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey('FGUser', db_column='updated_by', related_name='updated_by_diciplinaryactions_set', blank=True, null=True)
    created_by = models.ForeignKey('FGUser', db_column='created_by', related_name='created_by_diciplinaryactions_set', blank=True, null=True)
    cashier_created_by = models.ForeignKey('FGUser', db_column='cashier_created_by',
        related_name='cashier_created_by_diciplinaryactions_set',
        blank=True, null=True)
    cashier_updated_by = models.ForeignKey('FGUser', db_column='cashier_updated_by',
        related_name='cashier_updated_by_diciplinaryactions_set',
        blank=True, null=True)

    class Meta:
        db_table = 'disciplinary_actions'


class DiscountName(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    available = models.NullBooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'discount_names'


class DiscountPercentage(models.Model):
    percentage = models.IntegerField(blank=True, null=True)
    available = models.NullBooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'discount_percentages'


class DisktestBatchDrive(models.Model):
    serial_number = models.CharField(max_length=255)
    system_serial_number = models.CharField(max_length=255, blank=True, null=True)
    destroyed_at = models.DateTimeField(blank=True, null=True)
    user_destroyed_by = models.ForeignKey('FGUser', blank=True, null=True)
    disktest_run_id = models.IntegerField(blank=True, null=True)
    disktest_batch_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'disktest_batch_drives'


class DisktestBatch(models.Model):
    contact_id = models.IntegerField()
    name = models.CharField(max_length=255)
    date = models.DateField()
    finalized_on = models.DateField(blank=True, null=True)
    user_finalized_by = models.ForeignKey('FGUser', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'disktest_batches'


class DisktestRun(models.Model):
    vendor = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    serial_number = models.CharField(max_length=255, blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    result = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    megabytes_size = models.IntegerField(blank=True, null=True)
    bus_type = models.CharField(max_length=255, blank=True, null=True)
    failure_details = models.CharField(max_length=255, blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    log = models.TextField(blank=True, null=True)
    form_factor = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'disktest_runs'


class Donation(models.Model):
    contact_id = models.IntegerField(blank=True, null=True)
    postal_code = models.CharField(max_length=25, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('FGUser', related_name='created_by_donations_set', db_column='created_by')
    updated_by = models.ForeignKey('FGUser', related_name='updated_by_donations_set', db_column='updated_by', blank=True, null=True)
    reported_required_fee_cents = models.IntegerField(blank=True, null=True)
    reported_suggested_fee_cents = models.IntegerField(blank=True, null=True)
    needs_attention = models.BooleanField()
    invoice_resolved_at = models.DateTimeField(blank=True, null=True)
    contract_id = models.IntegerField()
    cashier_created_by = models.ForeignKey('FGUser', db_column='cashier_created_by',
        related_name='cashier_created_by_donations_set',
        blank=True, null=True)
    cashier_updated_by = models.ForeignKey('FGUser', db_column='cashier_updated_by',
        related_name='cashier_updated_by_donations_set',
        blank=True, null=True)
    adjustment = models.BooleanField()
    occurred_at = models.DateTimeField()
    is_pickup = models.BooleanField()
    reported_resolved_invoices_cents = models.IntegerField()
    reported_recycling_fees_cents = models.IntegerField()
    reported_pickup_fees_cents = models.IntegerField()
    reported_education_fees_cents = models.IntegerField()
    reported_tech_support_fees_cents = models.IntegerField()
    reported_other_fees_cents = models.IntegerField()

    class Meta:
        db_table = 'donations'


class EngineSchemaInfo(models.Model):
    engine_name = models.CharField(max_length=255, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'engine_schema_info'


class Generic(models.Model):
    value = models.CharField(max_length=100)
    only_serial = models.BooleanField()
    usable = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'generics'


class GizmoCategory(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'gizmo_categories'


class GizmoContext(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'gizmo_contexts'


class GizmoContextsGizmoType(models.Model):
    gizmo_context_id = models.IntegerField()
    gizmo_type_id = models.IntegerField()
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'gizmo_contexts_gizmo_types'


class GizmoEvent(models.Model):
    donation_id = models.IntegerField(blank=True, null=True)
    sale_id = models.IntegerField(blank=True, null=True)
    disbursement_id = models.IntegerField(blank=True, null=True)
    recycling_id = models.IntegerField(blank=True, null=True)
    gizmo_type_id = models.IntegerField()
    gizmo_context_id = models.IntegerField()
    gizmo_count = models.IntegerField()
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    occurred_at = models.DateTimeField(blank=True, null=True)
    unit_price_cents = models.IntegerField(blank=True, null=True)
    as_is = models.NullBooleanField()
    description = models.TextField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    recycling_contract_id = models.IntegerField(blank=True, null=True)
    system = models.ForeignKey('System', blank=True, null=True)
    covered = models.NullBooleanField()
    gizmo_return_id = models.IntegerField(blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    tester = models.CharField(max_length=255, blank=True, null=True)
    return_sale_id = models.IntegerField(blank=True, null=True)
    return_store_credit = models.ForeignKey('StoreCredit', blank=True, null=True)
    return_disbursement_id = models.IntegerField(blank=True, null=True)
    invoice_donation_id = models.IntegerField(blank=True, null=True)
    discount_percentage_id = models.IntegerField(blank=True, null=True)
    store_pricing = models.ForeignKey('StorePricing', blank=True, null=True)

    class Meta:
        db_table = 'gizmo_events'


class GizmoReturn(models.Model):
    contact_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    storecredit_difference_cents = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    cashier_created_by = models.ForeignKey('FGUser', db_column='cashier_created_by',
        related_name='cashier_created_by_gizmoreturns_set',
        blank=True, null=True)
    cashier_updated_by = models.ForeignKey('FGUser', db_column='cashier_updated_by',
        related_name='cashier_updated_by_gizmoreturns_set',
        blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    adjustment = models.BooleanField()
    occurred_at = models.DateTimeField()
    postal_code = models.CharField(max_length=25, blank=True, null=True)
    payment_method_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'gizmo_returns'


class GizmoTypeGroup(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'gizmo_type_groups'


class GizmoTypeGroupsGizmoType(models.Model):
    gizmo_type_id = models.IntegerField(blank=True, null=True)
    gizmo_type_group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'gizmo_type_groups_gizmo_types'


class GizmoType(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    required_fee_cents = models.IntegerField()
    suggested_fee_cents = models.IntegerField()
    gizmo_category_id = models.IntegerField()
    name = models.CharField(max_length=40)
    covered = models.NullBooleanField()
    rank = models.IntegerField(blank=True, null=True)
    effective_on = models.DateTimeField(blank=True, null=True)
    ineffective_on = models.DateTimeField(blank=True, null=True)
    parent_name = models.CharField(max_length=255, blank=True, null=True)
    needs_id = models.BooleanField()
    return_policy_id = models.IntegerField(blank=True, null=True)
    not_discounted = models.BooleanField()
    sales_limit = models.IntegerField(blank=True, null=True)
    tax_value_for_2014_cents = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'gizmo_types'


# class Holiday(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True)
#     holiday_date = models.DateField(blank=True, null=True)
#     is_all_day = models.NullBooleanField()
#     start_time = models.TimeField(blank=True, null=True)
#     end_time = models.TimeField(blank=True, null=True)
#     frequency_type_id = models.IntegerField(blank=True, null=True)
#     schedule_id = models.IntegerField(blank=True, null=True)
#     weekday = models.ForeignKey('Weekday', blank=True, null=True)

#     class Meta:
#         db_table = 'holidays'


class IncomeStream(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'income_streams'


class Job(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    income_stream_id = models.IntegerField(blank=True, null=True)
    wc_category = models.ForeignKey('WcCategory', blank=True, null=True)
    program_id = models.IntegerField(blank=True, null=True)
    virtual = models.BooleanField()
    effective_on = models.DateField(blank=True, null=True)
    ineffective_on = models.DateField(blank=True, null=True)
    offsite = models.BooleanField()
    reason_cannot_log_hours = models.TextField(blank=True, null=True)
    fully_covered = models.BooleanField()

    class Meta:
        db_table = 'jobs'


class Log(models.Model):
    table_name = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    thing_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    cashier_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'logs'


class Mailing(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=100)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'mailings'


class MeetingMinder(models.Model):
    meeting_id = models.IntegerField(blank=True, null=True)
    days_before = models.IntegerField(blank=True, null=True)
    recipient = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    script = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    hour = models.IntegerField()

    class Meta:
        db_table = 'meeting_minders'


class MeetingsWorker(models.Model):
    meeting_id = models.IntegerField(blank=True, null=True)
    worker = models.ForeignKey('Worker', blank=True, null=True)

    class Meta:
        db_table = 'meetings_workers'


class NewsletterSubscriber(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'newsletter_subscribers'


class Note(models.Model):
    contact_id = models.IntegerField(blank=True, null=True)
    system = models.ForeignKey('System', blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'notes'


class PayPeriod(models.Model):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'pay_periods'


class PaymentMethod(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'payment_methods'


class Payment(models.Model):
    donation_id = models.IntegerField(blank=True, null=True)
    sale_id = models.IntegerField(blank=True, null=True)
    payment_method_id = models.IntegerField()
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    amount_cents = models.IntegerField(blank=True, null=True)
    coupon_details = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'payments'


class PluginSchemaInfo(models.Model):
    plugin_name = models.CharField(max_length=255, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'plugin_schema_info'


class PointsTrade(models.Model):
    from_contact_id = models.IntegerField(blank=True, null=True)
    to_contact_id = models.IntegerField(blank=True, null=True)
    points = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    cashier_created_by = models.IntegerField(blank=True, null=True)
    cashier_updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'points_trades'


class PostalCode(models.Model):
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'postal_codes'


class PricingData(models.Model):
    table_name = models.CharField(max_length=255, blank=True, null=True)
    printme_value = models.CharField(max_length=255, blank=True, null=True)
    lookup_type = models.CharField(max_length=255, blank=True, null=True)
    lookup_value = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'pricing_datas'


class PricingTypesType(models.Model):
    type = models.ForeignKey('Type', blank=True, null=True)
    pricing_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'pricing_types_types'


class Privilege(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    restrict = models.BooleanField()

    class Meta:
        db_table = 'privileges'


class PrivilegesRole(models.Model):
    privilege_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'privileges_roles'


class Program(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    volunteer = models.BooleanField()
    adoption_credit = models.BooleanField()

    class Meta:
        db_table = 'programs'


class RecyclingShipment(models.Model):
    contact_id = models.IntegerField()
    bill_of_lading = models.CharField(max_length=255)
    received_at = models.DateField()
    resolved_at = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'recycling_shipments'


class Recycling(models.Model):
    comments = models.TextField(blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    recycled_at = models.DateTimeField()
    needs_attention = models.BooleanField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    cashier_created_by = models.ForeignKey('FGUser', db_column='cashier_created_by',
        related_name='cashier_created_by_recyclings_set',
        blank=True, null=True)
    cashier_updated_by = models.ForeignKey('FGUser', db_column='cashier_updated_by',
        related_name='cashier_updated_by_recyclings_set',
        blank=True, null=True)
    adjustment = models.BooleanField()

    class Meta:
        db_table = 'recyclings'


class ReportLog(models.Model):
    report_name = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'report_logs'


class Resource(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'resources'


class ResourcesVolunteerDefaultEvent(models.Model):
    volunteer_default_event = models.ForeignKey('VolunteerDefaultEvent', blank=True, null=True)
    resource_id = models.IntegerField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    effective_at = models.DateField(blank=True, null=True)
    ineffective_at = models.DateField(blank=True, null=True)
    roster_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'resources_volunteer_default_events'


class ResourcesVolunteerEvent(models.Model):
    volunteer_event = models.ForeignKey('VolunteerEvent', blank=True, null=True)
    resource_id = models.IntegerField(blank=True, null=True)
    resources_volunteer_default_event_id = models.IntegerField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    roster_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'resources_volunteer_events'


class ReturnPolicy(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'return_policies'


# class Role(models.Model):
#     name = models.CharField(max_length=40, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     notes = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         db_table = 'roles'


class RolesFGUser(models.Model):
    user = models.ForeignKey('FGUser', blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'roles_fgusers'


class Roster(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    limit_shift_signup_by_program = models.BooleanField()
    contact_type_id = models.IntegerField(blank=True, null=True)
    restrict_to_every_n_days = models.IntegerField(blank=True, null=True)
    restrict_from_sked_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'rosters'


class RostersSked(models.Model):
    sked_id = models.IntegerField(blank=True, null=True)
    roster_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'rosters_skeds'


class RrItem(models.Model):
    rr_set_id = models.IntegerField(blank=True, null=True)
    repeats_every = models.IntegerField(blank=True, null=True)
    repeats_on = models.IntegerField(blank=True, null=True)
    weekday_0 = models.NullBooleanField()
    weekday_1 = models.NullBooleanField()
    weekday_2 = models.NullBooleanField()
    weekday_3 = models.NullBooleanField()
    weekday_4 = models.NullBooleanField()
    weekday_5 = models.NullBooleanField()
    weekday_6 = models.NullBooleanField()
    day_of_month_final = models.NullBooleanField()
    min_day_of_month = models.IntegerField(blank=True, null=True)
    max_day_of_month = models.IntegerField(blank=True, null=True)
    week_of_month_final = models.NullBooleanField()
    week_of_month_1 = models.NullBooleanField()
    week_of_month_2 = models.NullBooleanField()
    week_of_month_3 = models.NullBooleanField()
    week_of_month_4 = models.NullBooleanField()
    week_of_month_5 = models.NullBooleanField()
    month_of_year_01 = models.NullBooleanField()
    month_of_year_02 = models.NullBooleanField()
    month_of_year_03 = models.NullBooleanField()
    month_of_year_04 = models.NullBooleanField()
    month_of_year_05 = models.NullBooleanField()
    month_of_year_06 = models.NullBooleanField()
    month_of_year_07 = models.NullBooleanField()
    month_of_year_08 = models.NullBooleanField()
    month_of_year_09 = models.NullBooleanField()
    month_of_year_11 = models.NullBooleanField()
    month_of_year_10 = models.NullBooleanField()
    month_of_year_12 = models.NullBooleanField()

    class Meta:
        db_table = 'rr_items'


class RrSet(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    ineffective_date = models.DateField(blank=True, null=True)
    match_mode = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'rr_sets'


class SaleType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'sale_types'


class Sale(models.Model):
    contact_id = models.IntegerField(blank=True, null=True)
    postal_code = models.CharField(max_length=25, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('FGUser', db_column='created_by',
        related_name='created_by_sales_set')
    updated_by = models.ForeignKey('FGUser', db_column='updated_by',
        related_name='updated_by_sales_set',
        blank=True, null=True)
    reported_discount_amount_cents = models.IntegerField(blank=True, null=True)
    reported_amount_due_cents = models.IntegerField(blank=True, null=True)
    needs_attention = models.BooleanField()
    invoice_resolved_at = models.DateTimeField(blank=True, null=True)
    cashier_created_by = models.ForeignKey('FGUser', db_column='cashier_created_by',
        related_name='cashier_created_by_sales_set',
        blank=True, null=True)
    cashier_updated_by = models.ForeignKey('FGUser', db_column='cashier_updated_by',
        related_name='cashier_updated_by_sales_set',
        blank=True, null=True)
    adjustment = models.BooleanField()
    occurred_at = models.DateTimeField()
    sale_type_id = models.IntegerField()
    discount_name_id = models.IntegerField()
    discount_percentage_id = models.IntegerField()
    amount_real_money_paid_cents = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'sales'


class Schedule(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    ineffective_date = models.DateField(blank=True, null=True)
    repeats_every = models.IntegerField(blank=True, null=True)
    repeats_on = models.IntegerField(blank=True, null=True)
    generate_from = models.BooleanField()
    reference_from = models.BooleanField()

    class Meta:
        db_table = 'schedules'


class SchemaInfo(models.Model):
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schema_info'


class SchemaMigration(models.Model):
    version = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class Session(models.Model):
    session_id = models.CharField(max_length=255)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'sessions'


# class ShiftFootnote(models.Model):
#     weekday = models.ForeignKey('Weekday', blank=True, null=True)
#     schedule_id = models.IntegerField(blank=True, null=True)
#     note = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         db_table = 'shift_footnotes'


# class Shift(models.Model):
#     type = models.CharField(max_length=255, blank=True, null=True)
#     start_time = models.TimeField(blank=True, null=True)
#     end_time = models.TimeField(blank=True, null=True)
#     meeting_name = models.CharField(max_length=255, blank=True, null=True)
#     shift_date = models.DateField(blank=True, null=True)
#     effective_date = models.DateField(blank=True, null=True)
#     ineffective_date = models.DateField(blank=True, null=True)
#     all_day = models.NullBooleanField()
#     repeats_every = models.IntegerField(blank=True, null=True)
#     repeats_on = models.IntegerField(blank=True, null=True)
#     frequency_type_id = models.IntegerField(blank=True, null=True)
#     job_id = models.IntegerField(blank=True, null=True)
#     meeting_id = models.IntegerField(blank=True, null=True)
#     schedule_id = models.IntegerField(blank=True, null=True)
#     weekday = models.ForeignKey('Weekday', blank=True, null=True)
#     worker = models.ForeignKey('Worker', blank=True, null=True)
#     actual = models.NullBooleanField()
#     training = models.NullBooleanField()
#     proposed = models.BooleanField()
#     created_by = models.ForeignKey('FGUser', db_column='created_by',
#         related_name='created_by_shifts_set',
#         blank=True, null=True)
#     updated_by = models.ForeignKey('FGUser', db_column='updated_by',
#         related_name='updated_by_shifts_set',
#         blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     week_1_of_month = models.BooleanField()
#     week_2_of_month = models.BooleanField()
#     week_3_of_month = models.BooleanField()
#     week_4_of_month = models.BooleanField()
#     week_5_of_month = models.BooleanField()
#     offsite = models.BooleanField()
#     repeats_every_months = models.IntegerField()
#     repeats_on_months = models.IntegerField()
#     week = models.CharField(max_length=1, blank=True, null=True)

#     class Meta:
#         db_table = 'shifts'


class SkedjulnatorAccess(models.Model):
    user = models.ForeignKey('FGUser', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'skedjulnator_accesses'


class Sked(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    category_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'skeds'


class SpecSheetQuestionCondition(models.Model):
    spec_sheet_question_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True, null=True)
    expected_value = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'spec_sheet_question_conditions'


class SpecSheetQuestion(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    question = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        db_table = 'spec_sheet_questions'


class SpecSheetValue(models.Model):
    spec_sheet = models.ForeignKey('SpecSheet', blank=True, null=True)
    spec_sheet_question_id = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'spec_sheet_values'


class SpecSheet(models.Model):
    system = models.ForeignKey('System', blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    old_id = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey('Type')
    os = models.CharField(max_length=255, blank=True, null=True)
    flag = models.NullBooleanField()
    cleaned_output = models.TextField(blank=True, null=True)
    original_output = models.TextField(blank=True, null=True)
    cleaned_valid = models.NullBooleanField()
    original_valid = models.NullBooleanField()
    builder_task_id = models.IntegerField()

    class Meta:
        db_table = 'spec_sheets'


# class StandardShift(models.Model):
#     start_time = models.TimeField(blank=True, null=True)
#     end_time = models.TimeField(blank=True, null=True)
#     job_id = models.IntegerField(blank=True, null=True)
#     meeting_id = models.IntegerField(blank=True, null=True)
#     schedule_id = models.IntegerField(blank=True, null=True)
#     weekday = models.ForeignKey('Weekday', blank=True, null=True)
#     worker = models.ForeignKey('Worker', blank=True, null=True)
#     shift_date = models.DateField(blank=True, null=True)

#     class Meta:
#         db_table = 'standard_shifts'


class StoreCredit(models.Model):
    gizmo_return_id = models.IntegerField(blank=True, null=True)
    gizmo_event_id = models.IntegerField(blank=True, null=True)
    payment_id = models.IntegerField(blank=True, null=True)
    amount_cents = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'store_credits'


class StorePricing(models.Model):
    gizmo_type_id = models.IntegerField(blank=True, null=True)
    unit_price_cents = models.IntegerField(blank=True, null=True)
    system = models.ForeignKey('System', blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'store_pricings'


class System(models.Model):
    system_vendor = models.CharField(max_length=255, blank=True, null=True)
    system_model = models.CharField(max_length=255, blank=True, null=True)
    system_serial_number = models.CharField(max_length=255, blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    mobo_vendor = models.CharField(max_length=255, blank=True, null=True)
    mobo_model = models.CharField(max_length=255, blank=True, null=True)
    mobo_serial_number = models.CharField(max_length=255, blank=True, null=True)
    serial_number = models.CharField(max_length=255, blank=True, null=True)
    vendor = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    contract_id = models.IntegerField()
    covered = models.NullBooleanField()
    bug_correction = models.CharField(max_length=255, blank=True, null=True)
    previous = models.ForeignKey('self', blank=True, null=True)
    l1_cache_total = models.CharField(max_length=255, blank=True, null=True)
    l2_cache_total = models.CharField(max_length=255, blank=True, null=True)
    l3_cache_total = models.CharField(max_length=255, blank=True, null=True)
    processor_slot = models.CharField(max_length=255, blank=True, null=True)
    processor_product = models.CharField(max_length=255, blank=True, null=True)
    processor_speed = models.CharField(max_length=255, blank=True, null=True)
    north_bridge = models.CharField(max_length=255, blank=True, null=True)
    sixty_four_bit = models.NullBooleanField()
    virtualization = models.NullBooleanField()
    last_build = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'systems'


class TechSupportNote(models.Model):
    contact_id = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey('FGUser', db_column='created_by', related_name='created_techsupportnotes_set', blank=True, null=True)
    updated_by = models.ForeignKey('FGUser', db_column='updated_by', related_name='updated_techsupportnotes_set', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tech_support_notes'


class TillAdjustment(models.Model):
    till_type = models.ForeignKey('TillType', blank=True, null=True)
    till_date = models.DateField(blank=True, null=True)
    adjustment_cents = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'till_adjustments'


class TillType(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'till_types'


class Type(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('FGUser', db_column='created_by',
        related_name='created_by_types_set')
    updated_by = models.ForeignKey('FGUser', db_column='updated_by',
        related_name='updated_by_types_set')
    name = models.CharField(unique=True, max_length=40)
    gizmo_type_id = models.IntegerField(blank=True, null=True)
    active = models.BooleanField()

    class Meta:
        db_table = 'types'


class FGUser(models.Model):
    login = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    crypted_password = models.CharField(max_length=40, blank=True, null=True)
    salt = models.CharField(max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    remember_token = models.CharField(max_length=255, blank=True, null=True)
    remember_token_expires_at = models.DateTimeField(blank=True, null=True)
    contact_id = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey('self', db_column='created_by',
        related_name='created_by_users_set', blank=True, null=True)
    updated_by = models.ForeignKey('self', db_column='updated_by',
        related_name='updated_by_users_set',
        blank=True, null=True)
    cashier_code = models.IntegerField(blank=True, null=True)
    can_login = models.BooleanField()
    last_logged_in = models.DateField(blank=True, null=True)
    shared = models.BooleanField()
    reason_cannot_login = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'users'


# class Vacation(models.Model):
#     effective_date = models.DateField(blank=True, null=True)
#     ineffective_date = models.DateField(blank=True, null=True)
#     is_all_day = models.NullBooleanField()
#     start_time = models.TimeField(blank=True, null=True)
#     end_time = models.TimeField(blank=True, null=True)
#     worker = models.ForeignKey('Worker', blank=True, null=True)
#     created_by = models.ForeignKey(FGUser, db_column='created_by',
#         related_name='created_by_vacations_set',
#         blank=True, null=True)
#     updated_by = models.ForeignKey(FGUser, db_column='updated_by',
#         related_name='updated_by_vacations_set',
#         blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         db_table = 'vacations'


class VolunteerDefaultEvent(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    weekday_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    week = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'volunteer_default_events'


class VolunteerDefaultShift(models.Model):
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    slot_count = models.IntegerField(blank=True, null=True)
    volunteer_task_type = models.ForeignKey('VolunteerTaskType', blank=True, null=True)
    roster_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    volunteer_default_event = models.ForeignKey(VolunteerDefaultEvent, null=True)
    class_credit = models.NullBooleanField()
    description = models.CharField(max_length=255, blank=True, null=True)
    program_id = models.IntegerField(blank=True, null=True)
    not_numbered = models.BooleanField()
    stuck_to_assignment = models.BooleanField()
    effective_on = models.DateField(blank=True, null=True)
    ineffective_on = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'volunteer_default_shifts'


class VolunteerEvent(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    volunteer_default_event = models.ForeignKey(VolunteerDefaultEvent, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    nowalkins = models.BooleanField()

    class Meta:
        db_table = 'volunteer_events'


class VolunteerShift(models.Model):
    volunteer_default_shift = models.ForeignKey(VolunteerDefaultShift, blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    volunteer_task_type = models.ForeignKey('VolunteerTaskType', blank=True, null=True)
    slot_number = models.IntegerField(blank=True, null=True)
    roster_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    volunteer_event = models.ForeignKey(VolunteerEvent)
    class_credit = models.NullBooleanField()
    description = models.CharField(max_length=255, blank=True, null=True)
    program_id = models.IntegerField(blank=True, null=True)
    not_numbered = models.BooleanField()
    stuck_to_assignment = models.BooleanField()

    class Meta:
        db_table = 'volunteer_shifts'


class VolunteerTaskType(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)
    hours_multiplier = models.DecimalField(max_digits=10, decimal_places=3)
    instantiable = models.BooleanField()
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=40)
    effective_on = models.DateTimeField(blank=True, null=True)
    ineffective_on = models.DateTimeField(blank=True, null=True)
    program_id = models.IntegerField()
    adoption_credit = models.NullBooleanField()

    class Meta:
        db_table = 'volunteer_task_types'


class VolunteerTask(models.Model):
    contact_id = models.IntegerField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    lock_version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    community_service_type_id = models.IntegerField(blank=True, null=True)
    volunteer_task_type = models.ForeignKey(VolunteerTaskType, blank=True, null=True)
    date_performed = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(FGUser, db_column='created_by',
        related_name='created_by_volunteertasks_set')
    updated_by = models.ForeignKey(FGUser, db_column='updated_by',
        related_name='updated_by_volunteertasks_set',
        blank=True, null=True)
    cashier_created_by = models.ForeignKey(FGUser, db_column='cashier_created_by',
        related_name='cashier_created_by_volunteertasks_set',
        blank=True, null=True)
    cashier_updated_by = models.ForeignKey(FGUser, db_column='cashier_updated_by',
        related_name='cashier_updated_by_volunteertasks_set',
        blank=True, null=True)
    program_id = models.IntegerField()

    class Meta:
        db_table = 'volunteer_tasks'


class WarrantyLength(models.Model):
    system_type = models.CharField(max_length=255)
    box_source = models.CharField(max_length=255)
    os_type = models.CharField(max_length=255, blank=True, null=True)
    length = models.CharField(max_length=255)
    effective_on = models.DateField(blank=True, null=True)
    ineffective_on = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'warranty_lengths'


class WcCategory(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    rate_cents = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'wc_categories'


# class Weekday(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True)
#     short_name = models.CharField(max_length=255, blank=True, null=True)
#     is_open = models.NullBooleanField()
#     start_time = models.TimeField(blank=True, null=True)
#     end_time = models.TimeField(blank=True, null=True)
#     open_time = models.TimeField()
#     close_time = models.TimeField()

#     class Meta:
#         db_table = 'weekdays'


class WorkShiftFootnote(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'work_shift_footnotes'


# class WorkShift(models.Model):
#     kind = models.CharField(max_length=255)
#     start_time = models.TimeField(blank=True, null=True)
#     end_time = models.TimeField(blank=True, null=True)
#     meeting_name = models.CharField(max_length=255, blank=True, null=True)
#     shift_date = models.DateField(blank=True, null=True)
#     effective_date = models.DateField(blank=True, null=True)
#     ineffective_date = models.DateField(blank=True, null=True)
#     all_day = models.NullBooleanField()
#     repeats_every = models.IntegerField(blank=True, null=True)
#     repeats_on = models.IntegerField(blank=True, null=True)
#     frequency_type_id = models.IntegerField(blank=True, null=True)
#     job_id = models.IntegerField(blank=True, null=True)
#     meeting_id = models.IntegerField(blank=True, null=True)
#     schedule_id = models.IntegerField(blank=True, null=True)
#     shift_id = models.IntegerField(blank=True, null=True)
#     weekday = models.ForeignKey(Weekday, blank=True, null=True)
#     worker = models.ForeignKey('Worker', blank=True, null=True)
#     actual = models.NullBooleanField()
#     training = models.NullBooleanField()
#     proposed = models.NullBooleanField()
#     created_by = models.ForeignKey(FGUser, db_column='created_by',
#         related_name='created_by_workshifts_set',
#         blank=True, null=True)
#     updated_by = models.ForeignKey(FGUser, db_column='updated_by',
#         related_name='updated_by_workshifts_set',
#         blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     offsite = models.BooleanField()

#     class Meta:
#         db_table = 'work_shifts'


class WorkedShift(models.Model):
    worker = models.ForeignKey('Worker', blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    date_performed = models.DateField(blank=True, null=True)
    duration = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    offsite = models.NullBooleanField()

    class Meta:
        db_table = 'worked_shifts'


class WorkerType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'worker_types'


# class Worker(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True)
#     standard_weekly_hours = models.FloatField(blank=True, null=True)
#     weekly_admin_hours = models.FloatField(blank=True, null=True)
#     contact_id = models.IntegerField(blank=True, null=True)
#     sunday = models.FloatField(blank=True, null=True)
#     monday = models.FloatField(blank=True, null=True)
#     tuesday = models.FloatField(blank=True, null=True)
#     wednesday = models.FloatField(blank=True, null=True)
#     thursday = models.FloatField(blank=True, null=True)
#     friday = models.FloatField(blank=True, null=True)
#     saturday = models.FloatField(blank=True, null=True)
#     salaried = models.NullBooleanField()
#     pto_rate = models.FloatField(blank=True, null=True)
#     floor_hours = models.FloatField(blank=True, null=True)
#     ceiling_hours = models.FloatField(blank=True, null=True)
#     virtual = models.BooleanField()

#     class Meta:
#         db_table = 'workers'


# class WorkersWorkerType(models.Model):
#     worker = models.ForeignKey(Worker)
#     worker_type = models.ForeignKey(WorkerType)
#     effective_on = models.DateField(blank=True, null=True)
#     ineffective_on = models.DateField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         db_table = 'workers_worker_types'

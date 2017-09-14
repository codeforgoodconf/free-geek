# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import freegeek.models
import django.db.models.deletion
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('start_time', models.DateTimeField(verbose_name='start_time')),
                ('end_time', models.DateTimeField(verbose_name='end_time')),
                ('filled', models.BooleanField(verbose_name='filled')),
                ('proficiency', models.CharField(max_length=40, default='L1', choices=[('L1', 'Level 1'), ('L2', 'Level 2'), ('L3', 'Level 3')])),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('title', models.CharField(max_length=4, default='MRS', choices=[('MR', 'Mr'), ('MRS', 'Mrs'), ('MISS', 'Miss'), ('MS', 'Ms'), ('DR', 'Dr'), ('PROF', 'Prof'), ('REV', 'Rev'), ('NONE', 'None')])),
                ('phone', models.CharField(max_length=20, blank=True, null=True, validators=[django.core.validators.RegexValidator(regex='[0-9][0-9 ]+', message='Not a valid phone number')])),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(max_length=1, default='F', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])),
                ('proficiency', models.CharField(max_length=40, default='L1', choices=[('L1', 'Level 1'), ('L2', 'Level 2'), ('L3', 'Level 3')])),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', freegeek.models.ProfileManager()),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('location', models.ForeignKey(to='freegeek.Location')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='freegeek.Profile'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='station',
            field=models.ForeignKey(to='freegeek.Station'),
        ),
    ]

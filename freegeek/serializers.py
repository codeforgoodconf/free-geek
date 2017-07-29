from rest_framework import serializers
from diary.models import Customer, Resource, Treatment, Entry
# from django.db import models
# from django.contrib import admin


class CustomerSerializer(serializers.ModelSerializer):
    """
    INPUT: The ModelSerializer method from serializers
    USAGE: Takes the model and fields from Customer and serializes them
    OUTPUT: N/A
    """

    class Meta:
        model = Customer
        fields = ('username', 'title',  'first_name', 'last_name',
                  'gender', 'age', 'date_of_birth', 'phone',
                  'notes')


class ResourceSerializer(serializers.ModelSerializer):
    """
    INPUT: ModelSerializer method from serializers
    USAGE: Takes the model and fields from Customer and serializes them
    OUTPUT: N/A
    """

    class Meta:
        model = Resource
        fields = ('name', 'description')


class TreatmentSerializer(serializers.ModelSerializer):
    """
    INPUT: ModelSerializer method from serializers
    USAGE: Takes the model and fields from Treatment and serializes them
    OUTPUT: N/A
    """

    class Meta:
        model = Treatment
        fields = ('name', 'min_duration', 'resource_required')


class EntrySerializer(serializers.ModelSerializer):
    """
    INPUT: ModelSerializer method from serializers
    USAGE: Takes the model and fields from Entry and serializes them
    OUTPUT: N/A
    """

    class Meta:
        model = Entry
        fields = ('date', 'time', 'duration', 'notes', 'created', 'creator',
                  'customer', 'resource', 'treatment', 'edited', 'editor',
                  'cancelled', 'no_show')

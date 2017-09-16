from django.shortcuts import render
from diary.models import Customer, Resource, Treatment, Entry
from rest_framework import viewsets
from .serializers import CustomerSerializer, ResourceSerializer, TreatmentSerializer, EntrySerializer


def home(request):
    return render(request, 'home.html')


def diary(request):
    """
    INPUT: A request
    USAGE: To render the diary/home.html page with no context
    OUTPUT: A rendered diary/home.html page
    """
    context_dict = {}
    return render(request, 'diary/home.html', context_dict)


class CustomerViewSet(viewsets.ModelViewSet):
    """
    INPUT: The ModelViewSet method from viewsets
    USAGE: API endpoint that allows Customer objects to be viewed or edited
    OUTPUT: N/A
    """

    # You can filter results or order of queryset by modifying the queryset variable
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    """
    INPUT: The ModelViewSet method from viewsets
    USAGE: API endpoint that allows Resource objects to be viewed and edited
    OUTPUT: N/A
    """

    # You can filter results or order of queryset by modifying the queryset variable
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class TreatmentViewSet(viewsets.ModelViewSet):
    """
    INPUT: ModelViewSet method in viewsets
    USAGE: API endpoint that allows Treatment objects to be viewed and edited
    OUTPUT: N/A
    """

    # You can filter results or order of queryset by modifying the queryset variable
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer


class EntryViewSet(viewsets.ModelViewSet):
    """
    INPUT: ModelViewSet method in viewsets
    USAGE: API endpoint that allows Treatment objects to be viewed and edited
    OUTPUT: N/A
    """

    # You can filter results or order of queryset by modifying the queryset variable
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

# start mbrochmann

from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from django.http import HttpResponseRedirect
#using an older version of django that does not include this
#from django.urls import reverse 
from django.views import generic
from django.views.generic.base import TemplateView

from .models import *

# need the following imports for current form of "results"
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

class LocationIndexView(generic.ListView):
    template_name = 'freegeek/location_index.html'
    context_object_name = 'location_list'

    def get_queryset(self):
        """Return the list of Locations."""
        return Location.objects.order_by('name')

class StationIndexView(generic.ListView):
    template_name = 'freegeek/station_index.html'
    context_object_name = 'station_list'

    def get_queryset(self):
        """Return the list of Stations."""
        return Station.objects.order_by('name')

class IndexView(TemplateView):
    template_name = 'freegeek/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['location_list'] = Location.objects.order_by('name')
        context['station_list'] = Station.objects.order_by('name')
        return context


class LocationDetailView(generic.DetailView):
    model = Location
    #pk_url_kwarg = 'name'
    slug_field = 'name'
    template_name = 'freegeek/location_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(LocationDetailView, self).get_context_data(*args, **kwargs)
        context['station_list'] = Station.objects.filter(location__name = self.object.name).order_by('name')
        return context


class StationDetailView(generic.DetailView):
    model = Station
    #pk_url_kwarg = 'name'
    slug_field = 'name'
    template_name = 'freegeek/station_detail.html'
    print("HI")

    def get_object(self):
        return self.model.objects.get(name=self.kwargs['slug'],location__name=self.kwargs['locationslug'])

    def get_context_data(self, *args, **kwargs):
        context = super(StationDetailView, self).get_context_data(*args, **kwargs)
        context['appointment_list'] = Appointment.objects.filter(station__name = self.object.name, station__location__name = self.kwargs['locationslug']).order_by('start_time')
        return context

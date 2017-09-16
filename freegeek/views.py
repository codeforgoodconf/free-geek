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
# using an older version of django that does not include this
# the mysite/polls tutorial used django 1.11
#from django.urls import reverse 
from django.views import generic
from django.views.generic.base import TemplateView

from .models import *

# needed the following imports for current form of "results" in the mysite/polls tutorial
# not using them now, but leaving them in for later
from django.http import HttpResponse
from django.http import Http404
from django.template import loader


class IndexView(generic.ListView):
    """ 
    Show the list of Locations as links to the Detail Views for the Locations.
    See the template in freegeek/templates/freegeek for more.

    """
    template_name = 'freegeek/index.html'
    context_object_name = 'location_list'

    def get_queryset(self):
        """Return the list of Locations."""
        return Location.objects.order_by('name')


class LocationDetailView(generic.DetailView):
    """
    Show the list of Stations as links to the Detail Views for the Stations.
    See the template in freegeek/templates/freegeek for more.

    """
    model = Location
    # set slug_field so that the object (Location) is specified by its 'name'
    slug_field = 'name'
    template_name = 'freegeek/location_detail.html'

    def get_context_data(self, *args, **kwargs):
        """
        Overriding the get_context_data method so we can grab a list of stations.
        (The standard DetailView just grabs the single object, in this case, 
        the Location, as specified above.)

        """
        context = super(LocationDetailView, self).get_context_data(*args, **kwargs)
        context['station_list'] = Station.objects.filter(location__name = self.object.name).order_by('name')
        return context


class StationDetailView(generic.DetailView):
    """
    Show the list of Appointments.
    See the template in freegeek/templates/freegeek for more.

    """
    model = Station
    template_name = 'freegeek/station_detail.html'

    def get_object(self):
        """
        Overriding the get_object method because currently identifying the Station with its Location name 
        (Location names are unique)
        and with its Station name.
        (Station names are unique for a given Location, 
        but multiple Locations might have Stations with the same name.)

        Note, the **kwargs are specified in urls.py.

        Not sure why get_object does not contain *args and **kwargs in its arguments
        while get_context_data does. (???)

        """
        return self.model.objects.get(name=self.kwargs['slug'],location__name=self.kwargs['locationslug'])

    def get_context_data(self, *args, **kwargs):
        """
        Overriding the get_context_data method so we can grab a list of Appointments
        and specify the order of the list (currently, by start_time).
        (The standard DetailView just grabs the single object, in this case, 
        the Station, as specified above.)

        Note, the **kwargs are specified in urls.py.

        Not sure why get_object does not contain *args and **kwargs in its arguments
        while get_context_data does. (???)

        """
        context = super(StationDetailView, self).get_context_data(*args, **kwargs)
        context['appointment_list'] = Appointment.objects.filter(station__name = self.object.name, station__location__name = self.kwargs['locationslug']).order_by('start_time')
        return context

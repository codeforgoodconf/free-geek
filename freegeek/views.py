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

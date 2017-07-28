from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def diary(request):
    context_dict = {}
    return render(request, 'diary/home.html', context_dict)
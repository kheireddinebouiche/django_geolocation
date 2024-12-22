from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.

# Vue pour afficher la carte
def map_view(request):
    return render(request, 'maps.html')

# Vue pour fournir les données des positions en JSON
def locations_data(request):
    locations = Location.objects.all()
    locations_data = list(locations.values("id", "name", "latitude", "longitude"))
    return JsonResponse(locations_data, safe=False)
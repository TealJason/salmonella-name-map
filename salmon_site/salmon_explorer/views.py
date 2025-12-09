from django.shortcuts import render
import os
from django.conf import settings
from django.shortcuts import render

def explore_serovar(request):
    
    serovar_coordinates_geojson = os.path.join(os.path.dirname(__file__), "data", "serovar_coordinates.geojson")
    
    if request.method == "GET":
        return render(request, "salmon_explorer/explore.html", {
            "MAPBOX_TOKEN": settings.MAPBOX_API_KEY,
            "geoJson_data": serovar_coordinates_geojson
        })


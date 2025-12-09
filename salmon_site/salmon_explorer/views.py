from django.shortcuts import render
import os
from django.conf import settings
from django.shortcuts import render
import json

def explore_serovar(request):
    
    geojson_path = os.path.join(os.path.dirname(__file__), "data", "serovar_coordinates.geojson")

    with open(geojson_path, "r") as f:
        serovar_coordinates_geojson = json.load(f)

    if request.method == "GET":
        return render(request, "salmon_explorer/explore.html", {
            "MAPBOX_TOKEN": settings.MAPBOX_API_KEY,
            "geoJson_data": serovar_coordinates_geojson
        })


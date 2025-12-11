from django.shortcuts import render
import os
from django.conf import settings
from django.shortcuts import render
import json
from . utils import run_lookup_logic

def explore_serovar(request):
    
    geojson_path = os.path.join(os.path.dirname(__file__), "data", "serovar_coordinates.geojson")

    with open(geojson_path, "r") as f:
        serovar_coordinates_geojson = json.load(f)

    if request.method == "GET":
        return render(request, "salmon_explorer/explore.html", {
            "MAPBOX_TOKEN": settings.MAPBOX_API_KEY,
            "geoJson_data": serovar_coordinates_geojson
        })

    if request.method == "POST":
        lat = request.POST.get("lat")
        long = request.POST.get("long")
        place_name = request.POST.get("place_name")
        get_image = request.POST.get("get_image")

        lat = float(lat) if lat else None
        long = float(long) if long else None

        result, mapbox_image = run_lookup_logic(lat, long, place_name, get_image, verbose=True)

        status = 200 if "error" not in result else 400
        return render(request, "salmon_explorer/explore.html", {
            "result": result,
            "mapbox_image": mapbox_image,
            "MAPBOX_TOKEN": settings.MAPBOX_API_KEY,
            "geoJson_data": serovar_coordinates_geojson
        })

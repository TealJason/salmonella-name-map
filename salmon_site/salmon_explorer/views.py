from django.shortcuts import render # type: ignore
import os
from django.conf import settings # type: ignore
from django.shortcuts import render # type: ignore
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

        lat = float(lat) if lat else None
        long = float(long) if long else None

        result = run_lookup_logic(lat, long, place_name, None, verbose=True)

    
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return render(request, "salmon_explorer/partials/result.html", {
                "result": result,
                "MAPBOX_TOKEN": settings.MAPBOX_API_KEY,
                "geoJson_data": serovar_coordinates_geojson
            })

        # Non-AJAX fallback
        return render(request, "salmon_explorer/explore.html", {
            "result": result,
            "MAPBOX_TOKEN": settings.MAPBOX_API_KEY,
            "geoJson_data": serovar_coordinates_geojson
        })

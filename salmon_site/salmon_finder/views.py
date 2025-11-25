from django.shortcuts import render
from .utils import run_lookup_logic
import os
from django.conf import settings
from django.shortcuts import render

def find_serovar(request):
    if request.method == "GET":
        return render(request, "salmon_finder/search.html", {
            "MAPBOX_TOKEN": settings.MAPBOX_API_KEY
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
        return render(request, "salmon_finder/search.html", {
            "result": result,
            "mapbox_image": mapbox_image,
            "MAPBOX_TOKEN": settings.MAPBOX_API_KEY   # <-- YOU MUST ADD THIS
        })

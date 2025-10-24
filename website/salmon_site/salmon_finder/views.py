from django.shortcuts import render
from .utils import run_lookup_logic
import os

def index(request):
    return render(request, "salmon_finder/index.html")

def find_serovar(request):
    if request.method == "GET":
        return render(request, "salmon_finder/search.html")

    if request.method == "POST":
        lat = request.POST.get("lat")
        long = request.POST.get("long")
        place_name = request.POST.get("place_name")

        lat = float(lat) if lat else None
        long = float(long) if long else None

        result = run_lookup_logic(lat, long, place_name, verbose=True)

        # Pass result data to the same search template
        status = 200 if "error" not in result else 400
        return render(request, "salmon_finder/search.html", {"result": result})

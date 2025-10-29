
from django.shortcuts import render
from .utils import run_lookup_logic
import os

# Create your views here.


def find_antigen_formula(request):
    if request.method == "GET":
        return render(request, "antigen_finder/search.html")

    if request.method == "POST":
        o_antigen = request.POST.get("lat")
        h_antigen_p1 = request.POST.get("long")
        h_antigen_p2 = request.POST.get("place_name")

        lat = float(lat) if lat else None
        long = float(long) if long else None

        result = run_lookup_logic(o_antigen, h_antigen_p1, h_antigen_p2, verbose=True)

        # Pass result data to the same search template
        status = 200 if "error" not in result else 400
        return render(request, "antigen_finder/search.html", {"result": result})

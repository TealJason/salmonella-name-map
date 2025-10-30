
from django.shortcuts import render
from .utils import get_antigens_for_serovar
import os

# Create your views here.
def find_antigen_formula(request):
    if request.method == "POST":
        serovar_name = request.POST.get("serovar_name", "").strip()
        if not serovar_name:
            return render(request, "antigen_finder/search.html", {"result": None, "searched": True})

        result = get_antigens_for_serovar(serovar_name)
        return render(request, "antigen_finder/search.html", {"result": result, "searched": True})
    
    return render(request, "antigen_finder/search.html")

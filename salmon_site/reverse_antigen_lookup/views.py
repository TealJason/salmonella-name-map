from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .utils import get_antigens_for_serovar
import os

# Create your views here.
def get_serovar_from_formula(request):
    if request.method == "POST":
        antigenic_formula = request.POST.get("antigenic_formula", "").strip()
        if not antigenic_formula:
            return render(request, "reverse_antigen_lookup/search.html", {"result": None, "searched": True})

        result = get_antigens_for_serovar(antigenic_formula)
        return render(request, "reverse_antigen_lookup/search.html", {"result": result, "searched": True})
    
    return render(request, "reverse_antigen_lookup/search.html")

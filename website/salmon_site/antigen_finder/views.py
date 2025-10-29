
from django.shortcuts import render
from .utils import get_antigens_for_serovar
import os

# Create your views here.


def find_antigen_formula(request):
    if request.method == "GET":
        return render(request, "antigen_finder/search.html")

    if request.method == "POST":
        serovar_name = request.POST.get("serovar_name")

        result = get_antigens_for_serovar(serovar_name)

        # Pass result data to the same search template
        status = 200 if "error" not in result else 400
        return render(request, "antigen_finder/search.html", {"result": result})

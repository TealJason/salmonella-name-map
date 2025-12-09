from django.urls import path
from . import views

urlpatterns = [
    path("formula_to_serovar/", views.get_serovar_from_formula, name="reverse_antigen_lookup"),  # main app logic
]

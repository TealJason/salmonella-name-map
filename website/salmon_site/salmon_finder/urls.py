from django.urls import path

urlpatterns = [
    path("find-serovar/", views.find_serovar, name="serovar_finder"),  # main app logic
]

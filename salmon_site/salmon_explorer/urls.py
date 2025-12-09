from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("explore-serovar/", views.explore_serovar, name="serovar_explorer"),  # main app logic
]



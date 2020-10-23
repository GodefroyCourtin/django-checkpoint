from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path("", views.acceuil, name="acceuil"),
    path("travel/", views.travel, name="travel"),
]
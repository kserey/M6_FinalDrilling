from django.urls import path
from vehiculo.views import *

urlpatterns = [
    path("add/", VehiculoCreateView.as_view(), name="add"),
]
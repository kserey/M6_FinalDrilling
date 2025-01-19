from django.urls import path
from vehiculo.views import *
from . import views


urlpatterns = [
    path("add/", VehiculoCreateView.as_view(), name="add"),
    path("listado/", views.listado, name="listado"),
]
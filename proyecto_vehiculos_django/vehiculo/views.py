from django.shortcuts import render
from .forms import VehiculoForm
from .models import Vehiculo
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add(request):
    return render(request, 'add.html')


class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm    
    template_name = 'add.html'  # Ruta del template
    success_url = reverse_lazy('index')  # Redirigir al listado tras crear


from django.shortcuts import render
from .forms import VehiculoForm, CustomUserCreationForm
from .models import Vehiculo
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add(request):
    return render(request, 'add.html')

class VehiculoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Vehiculo
    form_class = VehiculoForm    
    template_name = 'add.html'  # Ruta del template
    success_url = reverse_lazy('index')  # Redirigir al listado tras crear

    login_url = 'login'
    redirect_field_name = 'next'
    permission_required = 'visualizar_catalogo'




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            try:
                permission = Permission.objects.get(codename='visualizar_catalogo')
                user.user_permissions.add(permission)
                user.save()
            except Permission.DoesNotExist:
                messages.error(request, 'Permiso no encontrado')
                return redirect('index')
            
            login(request, user)
            messages.success(request, 'Registro exitoso')
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def listar_vehiculos(request):
    vehiculos_bajos = Vehiculo.objects.filter(precio_lt=10000)
    vehiculos_medios = Vehiculo.objects.filter(precio_gte=10000, precio_lte=30000)
    vehiculos_altos = Vehiculo.objects.filter(precio_gt=30000)

    vehiculos = list(vehiculo.oject.all().values('marca', 'modelo', 'carroceria', 'motor', 'categoria', 'precio'))

    return render(request, 'listar_vehiculos.html', {
        'vehiculos': vehiculos,
        'vehiculos_bajos': vehiculos_bajos,
        'vehiculos_medios': vehiculos_medios,
        'vehiculos_altos': vehiculos_altos,
    })
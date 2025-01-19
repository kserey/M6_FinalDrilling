from django.shortcuts import render, redirect
from .forms import VehiculoForm, CustomUserCreationForm
from .models import Vehiculo
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.
def index(request):
    return render(request, 'index.html')

def add(request):
    return render(request, 'add.html')

def listado(request):
    return render(request, 'listado.html')

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

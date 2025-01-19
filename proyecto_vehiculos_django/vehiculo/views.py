from django.shortcuts import render
from .forms import VehiculoForm
from .models import Vehiculo
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission, User
from django.contrib import messages
from django.contrib.auth import login

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
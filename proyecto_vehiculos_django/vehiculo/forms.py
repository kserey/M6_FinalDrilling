from django.forms import ModelForm
from vehiculo.models import Vehiculo

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'carroceria', 'motor', 'categoria', 'precio']



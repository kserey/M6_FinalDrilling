from django.forms import ModelForm
from vehiculo.models import Vehiculo
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'carroceria', 'motor', 'categoria', 'precio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['marca'].widget.attrs.update({'class': 'form-select'})
        self.fields['categoria'].widget.attrs.update({'class': 'form-select'})


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'email','password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
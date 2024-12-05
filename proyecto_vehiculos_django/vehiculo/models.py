from django.db import models

# Create your models here.
marcas=(('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Toyota', 'Toyota'))

categoria=(('particular', 'particular'),  ('transporte', 'transporte'),('carga', 'carga'))


class Vehiculo(models.Model):
    marca = models.CharField(verbose_name='Marca', verbose_name_plural='Marcas', choices=marcas, max_length=20)
    modelo = models.CharField(verbose_name='Modelo',verbose_name_plural='Modelos', max_length=100)
    carroceria = models.CharField(verbose_name='Carrocería', verbose_name_plural='Carrocerías', max_length=50)
    motor = models.CharField(max_length=50)
    categoria = models.CharField(verbose_name='Categoría', verbose_name_plural='Categorías', choices=categoria, max_length=20)
    precio = models.IntegerField(verbose_name='Precio', verbose_name_plural='Precios')
    created = models.DateField(verbose_name='Fecha de creación',auto_now_add=True)
    updated = models.DateField(verbose_name='Fecha de actualización',auto_now=True)

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.carroceria}'
    
    

    
    
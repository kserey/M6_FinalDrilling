from django.db import models

class Vehiculo(models.Model):
    marcas=[
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'), 
        ('Ford', 'Ford'), 
        ('Toyota', 'Toyota')
    ]

    categoria=[
        ('particular', 'particular'),  
        ('transporte', 'transporte'),
        ('carga', 'carga')
    ]

    marca = models.CharField(verbose_name='Marca', choices=marcas, max_length=20, default='Ford')
    modelo = models.CharField(verbose_name='Modelo', max_length=100)
    carroceria = models.CharField(verbose_name='Carrocería', max_length=50)
    motor = models.CharField(max_length=50)
    categoria = models.CharField(verbose_name='Categoría', choices=categoria, max_length=20, default='particular')
    precio = models.IntegerField(verbose_name='Precio')
    created = models.DateField(verbose_name='Fecha de creación',auto_now_add=True)
    updated = models.DateField(verbose_name='Fecha de actualización',auto_now=True)   
    
class Meta:
    verbose_name = 'Vehiculo'
    verbose_name_plural = 'Vehiculos'
    permissions = [
        ('add_vehiculomodel', 'Puede agregar vehículos al catálogo'),
        ('visualizar_catalogo', 'Puede visualizar catálogo'),
                   ]
    
def __str__(self):
    return f'{self.marca} {self.modelo} {self.carroceria}'
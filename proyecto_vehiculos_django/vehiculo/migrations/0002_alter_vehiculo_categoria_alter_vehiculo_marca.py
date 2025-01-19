# Generated by Django 5.1.3 on 2025-01-19 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='categoria',
            field=models.CharField(choices=[('particular', 'particular'), ('transporte', 'transporte'), ('carga', 'carga')], default='particular', max_length=20, verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(choices=[('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Toyota', 'Toyota')], default='Ford', max_length=20, verbose_name='Marca'),
        ),
    ]

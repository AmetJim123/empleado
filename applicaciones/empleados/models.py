from django.db import models

#Datos de otro archivo py
from applicaciones.departamento.models import Departamento

# Aplicación de terceros
from ckeditor.fields import RichTextField 

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad

# Create your models here.
class Empleado(models.Model):
    """ Modelo para tabla empleado """

    JOB_CHOICES=(
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'ABOGADO'),
        ('4', 'INGENIERO'),
        ('5', 'COMUNITY MANAGER'),
        ('6', 'Otro'),
    )
    
    
    primer_nombre = models.CharField(
        'Nombre',
        max_length=50)
    
    primer_apellido = models.CharField(
        'Apellido', 
        max_length=50)

    nombre_completo = models.CharField(
        'Nombre completo',
         max_length=180,
         blank=True,
         null=True)

    trabajo = models.CharField(
        'Trabajo', 
        max_length=50, 
        choices=JOB_CHOICES)

    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE)

    avatar = models.ImageField(
        upload_to='empleado',
        blank=True,
        null=True)

    habilidades = models.ManyToManyField(
        Habilidades)

    hoja_vida = RichTextField(
        blank=True, 
        null=True)


    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']
        

    def __str__(self):
        return str(self.id) + ') ' + self.primer_nombre + '  ' + self.primer_apellido
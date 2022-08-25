from tabnanny import verbose
from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50,)
    short_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    inactivo = models.BooleanField('Este departamento está inactivo', default=False)

    class Meta:
        verbose_name = 'Mi departamento'
        verbose_name = 'Areas de la empresa'
        ordering = ['-id']
        unique_together = ('name', 'short_name')

    def __str__(self):
        return str(self.id) + ') ' + self.name + ' - ' + self.short_name


from django.db import models

# Create your models here.

class Prueba(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.titulo + '-' + self.subtitulo


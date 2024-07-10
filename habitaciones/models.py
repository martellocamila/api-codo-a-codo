from django.db import models

class Habitacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    precio = models.PositiveIntegerField()
    foto = models.ImageField(upload_to='foto_habitaciones/', null=True, blank=True)


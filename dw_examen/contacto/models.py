from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="", null=True, blank=True, width_field='ancho_imagen',height_field='alto_imagen')
    alto_imagen = models.IntegerField(default=0)
    ancho_imagen = models.IntegerField(default=0)

from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=164)
    subtitulo = models.CharField(max_length=164)
    cuerpo = models.CharField(max_length=254)
    autor = models.CharField(max_length=164)
    fecha = models.DateField()

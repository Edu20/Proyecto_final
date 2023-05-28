from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=164)
    subtitulo = models.CharField(max_length=164)
    cuerpo = models.CharField(max_length=254)
    autor = models.CharField(max_length=164)
    fecha = models.DateField()
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return  self.titulo
from django.contrib.auth.models import User
from django.test import TestCase
from articulos.models import Articulo

class ArticuloTests(TestCase):
    def test_creation_articulo_1(self):
        usuario = User.objects.create(username="nombre_usuario")
        articulo = Articulo(titulo="Este es el titulo", subtitulo="subtitulo", cuerpo="cuerpo", autor="autor", fecha="22-02-1995", creador=usuario)
        # Resto de las aserciones y acciones de prueba

    def test_creation_articulo_2(self):
        usuario = User.objects.create(username="nombre_usuario")
        articulo = Articulo(titulo="Este es el titulo", subtitulo="subtitulo", cuerpo="cuerpo", autor="autor", fecha="SERIAL-1", creador=usuario)
        # Resto de las aserciones y acciones de prueba
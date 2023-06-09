from django.contrib import admin
from django.urls import path
from articulos.views import listar_articulos, crear_articulo, buscar_articulos, eliminar_articulo, \
editar_articulo, detalle_articulo



urlpatterns = [
    path('articulos/', listar_articulos, name="lista_articulos"),
    path('crearArticulos/', crear_articulo, name="crear_articulos"),
    path('buscarArticulos/', buscar_articulos, name="buscar_articulos"),
    path('eliminarArticulos/<int:id>', eliminar_articulo, name="eliminar_articulos"),
    path('editarArticulos/<int:id>', editar_articulo, name="editar_articulos"),
    path('detalleArticulos/<int:id>', detalle_articulo, name="detalle_articulos"),
]
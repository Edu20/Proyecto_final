from django.contrib import admin
from django.urls import path
from articulos.views import listar_articulos, crear_articulo



urlpatterns = [
    path('articulos/', listar_articulos, name="lista_articulos"),
    path('crearArticulos/', crear_articulo, name="crear_articulos"),
]
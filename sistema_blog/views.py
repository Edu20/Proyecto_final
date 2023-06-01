from django.shortcuts import render
from django.http import HttpResponse
from articulos.models import Articulo
from datetime import datetime



def saludo(request):
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html  


def inicio(request):
    contexto = {
        "articulos": Articulo.objects.all()
    }
    http_response = render(
        request=request,
        template_name="articulos/index.html",
        context=contexto
    )
    return http_response


def about(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name="articulos/about.html",
        context=contexto
    )
    return http_response
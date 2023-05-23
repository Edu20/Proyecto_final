from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime



def saludo(request):
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html  


def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name="articulos/index.html",
        context=contexto
    )
    return http_response
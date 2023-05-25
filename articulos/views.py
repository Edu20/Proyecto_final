from django.shortcuts import render, redirect
from articulos.models import Articulo
from articulos.forms import ArticuloFormulario
from django.urls import reverse
# Create your views here.

def listar_articulos(request):
    contexto = {
        "articulos": Articulo.objects.all()
    }
    http_response = render(
        request=request,
        template_name='articulos/lista_articulos.html',
        context=contexto,
    )
    return http_response


def crear_articulo(request):
    if request.method == "POST":
        formulario = ArticuloFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data # es un diccionario
            titulo = data["titulo"]
            subtitulo = data["subtitulo"]
            cuerpo = data["cuerpo"]
            autor = data["autor"]
            fecha = data["fecha"]
            articulo = Articulo(titulo=titulo,subtitulo=subtitulo,cuerpo=cuerpo,autor=autor,fecha=fecha) #se crea en RAM
            articulo.save() #se guarda en la base de datos 
            url_exitosa = reverse('lista_articulos')
            return redirect(url_exitosa)
        
    
    else:
        formulario =ArticuloFormulario()
        http_response = render(
        request=request,
        template_name="articulos/formulario_articulo.html",
        context={'formulario':formulario}
        )
        return http_response
    
def buscar_articulos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        articulos = Articulo.objects.filter(titulo__contains=busqueda)
        contexto = {
            "articulos":articulos,
        }
    http_response = render(
        request=request,
        template_name='articulos/lista_articulos.html',
        context=contexto
    )
    return http_response
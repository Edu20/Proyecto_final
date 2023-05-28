from django.shortcuts import render, redirect
from articulos.models import Articulo
from articulos.forms import ArticuloFormulario
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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


@login_required
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
            creador = request.user 
            articulo = Articulo(titulo=titulo,subtitulo=subtitulo,cuerpo=cuerpo,autor=autor,fecha=fecha, creador=creador) #se crea en RAM
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
    contexto = {}
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        articulos = Articulo.objects.filter(titulo=busqueda)
        contexto = {
            "articulos":articulos,
        }
    http_response = render(
        request=request,
        template_name='articulos/lista_articulos.html',
        context=contexto
    )
    return http_response


@login_required
def eliminar_articulo(request, id):
    articulo = Articulo.objects.get(id=id)
    if request.method == "POST":
        articulo.delete()
        url_exitosa = reverse('lista_articulos')
        return redirect(url_exitosa)
    else:
            # Procesar la solicitud GET para mostrar una confirmación de eliminación
        articulo = Articulo.objects.get(id=id)
        return render(request, 'articulos/eliminar_articulo.html', {'articulo': articulo})


@login_required
def editar_articulo(request, id):
    articulo = Articulo.objects.get(id=id)
    if request.method == "POST":
        formulario = ArticuloFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            articulo.titulo = data["titulo"]
            articulo.subtitulo = data["subtitulo"]
            articulo.cuerpo = data["cuerpo"]
            articulo.autor = data["autor"]
            articulo.fecha = data["fecha"]
            articulo.save()
            url_exitosa = reverse('lista_articulos')
            return redirect(url_exitosa)
    
    else:
        inicial = {
            'titulo': articulo.titulo,
            'subtitulo': articulo.subtitulo,
            'cuerpo': articulo.cuerpo,
            'autor': articulo.autor,
            'fecha': articulo.fecha
        }
        formulario = ArticuloFormulario(initial=inicial)
    return render(
        request=request,
        template_name= 'articulos/formulario_articulo.html',
        context={'formulario':formulario},
        )


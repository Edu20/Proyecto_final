from django import forms

class ArticuloFormulario(forms.Form):
    titulo = forms.CharField(max_length=164)
    subtitulo = forms.CharField(max_length=164)
    cuerpo = forms.CharField(max_length=254)
    autor = forms.CharField(max_length=164)
    fecha = forms.DateField(input_formats=["%d/%m/%Y"])
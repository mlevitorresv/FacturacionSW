from django.shortcuts import render, redirect
from CoronaCastilla.models import Articulo

def view_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'articulos.html', {'articulos' : articulos})
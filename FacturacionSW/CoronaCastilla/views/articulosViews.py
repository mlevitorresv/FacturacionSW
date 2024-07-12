from django.shortcuts import render, redirect
from django.http import JsonResponse
from CoronaCastilla.models import Articulo


def view_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'articulos.html', {'articulos' : articulos})

def get_precios(request):
    tipo_habitacion = request.GET.get('tipoHabitacion')
    articulo = Articulo.objects.filter(nombre=tipo_habitacion).first()
    data = {}
    if articulo:
        data = {
            'precio1': articulo.precio1,
            'precio2': articulo.precio2,
            'precio3': articulo.precio3,
            'precio4': articulo.precio4
        }
    return JsonResponse(data)
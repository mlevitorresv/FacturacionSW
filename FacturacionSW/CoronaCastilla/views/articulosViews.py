from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from CoronaCastilla.models import Articulo
from CoronaCastilla.forms import articuloEditForm


def view_articulos(request):
    articulos = Articulo.objects.all()
    forms = [articuloEditForm(instance=articulo) for articulo in articulos]

    if request.method == 'POST':
        for articulo, form in zip(articulos, forms):
            form = articuloEditForm(request.POST, instance=articulo)
            if form.is_valid():
                form.save()

    context = {
        'articulos': zip(articulos, forms),
    }
    return render(request, 'articulos.html', context)

def actualizar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)

    if request.method == 'POST':
        form = articuloEditForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('articulos')  # Redirige a la lista de artículos después de actualizar
    else:
        form = articuloEditForm(instance=articulo)
    
    context = {
        'form': form,
        'articulo': articulo,
    }
    return render(request, 'actualizar_articulo.html', context)



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
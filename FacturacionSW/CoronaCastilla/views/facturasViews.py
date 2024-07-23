from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q, Sum
from CoronaCastilla.models import Factura, Articulo
from CoronaCastilla.forms import facturaForm, getFacturas
from datetime import datetime


def view_facturas(request):
    if request.method == 'GET':
        form = getFacturas(request.GET)
        
    filtro = request.GET.get('select_facturas')
    
    ahora = datetime.now()
    mes_actual = ahora.month
    año_actual = ahora.year
        
    
    if filtro == 'mes':
        facturas = Factura.objects.filter(fecha_salida__year =año_actual, fecha_salida__month=mes_actual)
    
    elif filtro == 'meses':
        meses = [mes_actual, (mes_actual - 1) % 12 or 12, (mes_actual - 2) % 12 or 12]
        años = [año_actual] * 3
        
        if mes_actual == 1:
            años[1] -= 1
            años[2] -= 1
        elif mes_actual == 2:
            años[2] -= 1

        query = Q(fecha_salida__year=años[0], fecha_salida__month=meses[0]) | \
                Q(fecha_salida__year=años[1], fecha_salida__month=meses[1]) | \
                Q(fecha_salida__year=años[2], fecha_salida__month=meses[2])
        facturas = Factura.objects.filter(query)
    else:
        facturas = Factura.objects.all()
        
    total_facturado = facturas.aggregate(Sum('total_factura'))['total_factura__sum'] or 0

        
        
    return render(request, 'facturas.html', {'facturas' : facturas, 'form':form, 'total_facturado': total_facturado})



def view_factura_id(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
        
    if request.method == 'POST':
        form = facturaForm(request.POST, instance=factura)
        if form.is_valid():
            form.save()
            return redirect('facturas')
    else:
        form = facturaForm(instance=factura)
        
    alojamiento_result = factura.alojamiento_dias * factura.alojamiento_precio
    desayuno_result = factura.desayuno_dias * factura.desayuno_precio

    context = {
        'factura': factura,
        'alojamiento_result': alojamiento_result,
        'desayuno_result': desayuno_result,
        'form': form
    }
    
    return render(request, 'gestionarFactura.html', context)
    
    

def post_factura(request):
    articulos = Articulo.objects.all()  # Obtener todos los artículos disponibles
    form = facturaForm(request.POST or None)

    if request.method == 'POST':
        # Cargar dinámicamente las opciones antes de la validación
        tipo_habitacion = request.POST.get('tipoHabitacion')
        tipo_desayuno = 'desayuno'
        
        if tipo_habitacion:
            articulo_habitacion = Articulo.objects.filter(nombre=tipo_habitacion).first()
            if articulo_habitacion:
                precios_habitacion = [
                    (float(articulo_habitacion.precio1), '€' + str(float(articulo_habitacion.precio1))),
                    (float(articulo_habitacion.precio2), '€' + str(float(articulo_habitacion.precio2))),
                    (float(articulo_habitacion.precio3), '€' + str(float(articulo_habitacion.precio3))),
                    (float(articulo_habitacion.precio4), '€' + str(float(articulo_habitacion.precio4))),
                ]
                form.fields['alojamiento_precio'].choices = precios_habitacion

        if tipo_desayuno:
            articulo_desayuno = Articulo.objects.filter(nombre=tipo_desayuno).first()
            if articulo_desayuno:
                precios_desayuno = [
                    (float(articulo_desayuno.precio1), '€' + str(float(articulo_desayuno.precio1))),
                    (float(articulo_desayuno.precio2), '€' + str(float(articulo_desayuno.precio2))),
                    (float(articulo_desayuno.precio3), '€' + str(float(articulo_desayuno.precio3))),
                    (float(articulo_desayuno.precio4), '€' + str(float(articulo_desayuno.precio4))),
                ]
                form.fields['desayuno_precio'].choices = precios_desayuno

        if form.is_valid():
            factura = form.save(commit=False)
            
            tipo_habitacion = form.cleaned_data.get('tipoHabitacion')
            habitacion = Articulo.objects.filter(nombre=tipo_habitacion).first()
            
            if habitacion:
                factura.habitacion = habitacion
            
            # Guardar la factura después de asignar habitacion_id
            factura.save()
            
            return redirect('index')  # Redirigir a la lista de facturas después de guardar
        else:
            print('formulario invalido', form.errors)

    return render(request, 'crearFactura.html', {'form': form, 'articulos': articulos})




def delete_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    
    if request.method == 'POST':
        factura.delete()
        return redirect('facturas')  # Redirige a la lista de facturas después de eliminar
    
    # Si no es una solicitud POST, renderiza la página de detalles de factura (o alguna otra vista)
    return render(request, 'gestionarFactura.html', {'factura': factura})

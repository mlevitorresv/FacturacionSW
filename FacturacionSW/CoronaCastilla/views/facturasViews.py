from django.shortcuts import render, redirect
from django.db.models import Q
from CoronaCastilla.models import Factura, Articulo
from CoronaCastilla.forms import facturaForm
from datetime import datetime

def view_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'facturas.html', {'facturas' : facturas})

def view_facturas_ultimo(request):
    ahora = datetime.now()
    mes_actual = ahora.month
    año_actual = ahora.year
    
    facturas = Factura.objects.filter(fecha_salida__year =año_actual, fecha_salida__month=mes_actual)
    return render(request, 'facturas.html', {'facturas' : facturas})

def view_facturas_tres(request):
    ahora = datetime.now()
    mes_actual = ahora.month
    año_actual = ahora.year
    
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
    return render(request, 'facturas.html', {'facturas' : facturas})


def view_factura_id(request, factura_id):
    factura = Factura.objects.get(id=factura_id)
    
    alojamiento_importe = factura.alojamiento_dias * factura.alojamiento_precio
    desayuno_importe = factura.desayuno_dias * factura.desayuno_precio
    porcentaje_iva = int(factura.porcentaje_iva)
    fecha_entrada = datetime.strptime(str(factura.fecha_entrada) , '%Y-%m-%d').strftime('%Y-%m-%d')
    fecha_salida = datetime.strptime(str(factura.fecha_salida) , '%Y-%m-%d').strftime('%Y-%m-%d')
    
    context = {
        'factura': factura,
        'alojamiento_importe': alojamiento_importe,
        'desayuno_importe': desayuno_importe,
        'porcentaje_iva': porcentaje_iva,
        'fecha_entrada': fecha_entrada,
        'fecha_salida': fecha_salida,
    }
    
    return render(request, 'gestionarFactura.html', context)


def post_factura(request):
    articulos = Articulo.objects.all()  # Obtener todos los artículos disponibles
    if request.method == 'POST':
        form = facturaForm(request.POST)
        # Cargar dinámicamente las opciones antes de la validación
        tipo_habitacion = request.POST.get('tipoHabitacion')
        if tipo_habitacion:
            articulo = Articulo.objects.filter(nombre=tipo_habitacion).first()
            if articulo:
                precios = [
                    (float(articulo.precio1), '€' + str(float(articulo.precio1))),
                    (float(articulo.precio2), '€' + str(float(articulo.precio2))),
                    (float(articulo.precio3), '€' + str(float(articulo.precio3))),
                    (float(articulo.precio4), '€' + str(float(articulo.precio4))),
                ]
                form.fields['alojamiento_precio'].choices = precios
                form.fields['desayuno_precio'].choices = precios
        if form.is_valid():
            form.save()  # Guardar el formulario si es válido
            return redirect('facturasViews.view_facturas')  # Redirigir a la lista de facturas después de guardar
        else:
            print('formulario invalido', form.errors)
    else:
        form = facturaForm()  # Formulario vacío para mostrar en GET
    
    return render(request, 'crearFactura.html', {'form': form, 'articulos': articulos})
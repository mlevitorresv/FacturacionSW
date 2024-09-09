from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q, Sum
from CoronaCastilla.models import Factura
from CoronaCastilla.forms import facturaForm, facturaForm, getFacturas
from datetime import datetime


from django.shortcuts import render
from django.db.models import Sum, Q
from datetime import datetime
import re

def extract_name(cliente_text):
    # Encuentra el NIF en el texto usando una expresión regular
    match = re.search(r'\d{8}[A-Z]', cliente_text)
    if match:
        pos_nif = match.start()
        # Extraer el nombre del texto
        return cliente_text[:pos_nif].strip()
    return cliente_text

def view_facturas(request):
    if request.method == 'GET':
        form = getFacturas(request.GET)
        
    filtro = request.GET.get('select_facturas')
    
    ahora = datetime.now()
    mes_actual = ahora.month
    año_actual = ahora.year
        
    if filtro == 'mes':
        facturas = Factura.objects.filter(fecha_salida__year=año_actual, fecha_salida__month=mes_actual)
    
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

    # Extraer el nombre del cliente para cada factura
    for factura in facturas:
        factura.cliente_nombre = extract_name(factura.cliente)

    return render(request, 'facturas.html', {'facturas': facturas, 'form': form, 'total_facturado': total_facturado})



def view_factura_id(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
        
    if request.method == 'POST':
        form = facturaForm(request.POST, instance=factura)
        if factura['fecha_creacion'] - datetime.date.today() > 2:
            return '<script>alert("No se puede modificar la factura por: CIERRE DE CAJA")</script>'
        
        if form.is_valid():
            form.save()
            return redirect('facturas')
        else:
            print(form.fields['alojamiento_precio'].choices)
            print(request.POST)
            print(form.errors)
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
    form = facturaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            factura = form.save(commit=False)            
            factura.save()
            
            return redirect('facturas')  # Redirigir a la lista de facturas después de guardar
        else:
            print('formulario invalido', form.errors)

    return render(request, 'crearFactura.html', {'form': form})




def delete_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    
    if request.method == 'POST':
        factura.delete()
        return redirect('facturas')  # Redirige a la lista de facturas después de eliminar
    
    # Si no es una solicitud POST, renderiza la página de detalles de factura (o alguna otra vista)
    return render(request, 'gestionarFactura.html', {'factura': factura})

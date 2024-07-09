from django.shortcuts import render, redirect
from CoronaCastilla.models import Factura
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
    
    facturas = Factura.objects.filter(fecha_salida__year =año_actual, fecha_salida__month=mes_actual, fecha_salida__month=mes_actual - 1, fecha_salida__month=mes_actual - 2)
    return render(request, 'facturas.html', {'facturas' : facturas})


def view_factura_id(request, factura_id):
    factura = Factura.objects.get(id=factura_id)
    return render(request, 'facturaDetails.html', {'factura' : factura})


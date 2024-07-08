from django.shortcuts import render, redirect
from CoronaCastilla.models import Factura

def view_facturas():
    return render('facturas.html')

def view_factura_id(request, factura_id):
    factura = Factura.objects.get(id=factura_id)
    return render(request, 'facturaDetails.html', {'factura' : factura})


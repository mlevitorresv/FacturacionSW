from django.shortcuts import render, redirect
from CoronaCastilla.models import Factura

def view_articulos():
    return render('articulos.html')
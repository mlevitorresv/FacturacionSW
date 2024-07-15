"""
URL configuration for FacturacionSW project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CoronaCastilla.views import indexViews, facturasViews, articulosViews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", indexViews.view_index, name='index'),
    path("facturas", facturasViews.view_facturas, name='facturas'),
    path("facturas/<int:factura_id>", facturasViews.view_factura_id, name='facturaDetails'),
    path("facturas/nueva", facturasViews.post_factura, name='nuevaFactura'),
    path("facturas/edit/<int:factura_id>", facturasViews.view_facturas, name='editaFactura'),
    path("facturas/delete/<int:factura_id>", facturasViews.delete_factura, name='eliminaFactura'),
    path("articulos", articulosViews.view_articulos, name='articulos'),
    path('articulos/<int:articulo_id>/actualizar/', articulosViews.actualizar_articulo, name='actualizar_articulo'),
    path('get-precios/', articulosViews.get_precios, name='get_precios')    
]

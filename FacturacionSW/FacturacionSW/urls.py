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
from CoronaCastilla.views import indexViews, facturasViews, clientesViews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", indexViews.view_index, name='index'),
    # rutas de facturas
    path("facturas", facturasViews.view_facturas, name='facturas'),
    path("facturas/<int:factura_id>", facturasViews.view_factura_id, name='facturaDetails'),
    path("facturas/nueva", facturasViews.post_factura, name='nuevaFactura'),
    path("facturas/<int:factura_id>/edit", facturasViews.view_factura_id, name='editaFactura'),
    path("facturas/<int:factura_id>/delete", facturasViews.delete_factura, name='eliminaFactura'),
    path('facturas/<int:factura_id>/cerrar/', facturasViews.close_factura, name='cerrar_factura'),
    path('facturas/cerrar/', facturasViews.close_new_factura, name='cerrar_factura_sin_id'),


    #ruta para descargar resumen
    path('exportar-facturas/<str:cliente>/<int:mes_actual>/<int:año_actual>/', facturasViews.generate_excel, name='exportar_facturas'),
    
    # rutas de clientes
    path("clientes", clientesViews.view_clientes, name='clientes'),
    path("clientes/<int:cliente_id>", clientesViews.view_cliente_id, name='clienteDetails'),
    path("clientes/nuevo", clientesViews.post_cliente, name='nuevoCliente'),
    path("clientes/<int:cliente_id>/edit", clientesViews.view_cliente_id, name='editaCliente'),
    path("clientes/<int:cliente_id>/delete", clientesViews.delete_cliente, name='eliminaCliente'),
    
    #rutas de cliente (JSON)
    path('get_cliente/<int:cliente_id>/', clientesViews.get_cliente, name='get_cliente'),

]

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.db.models import Q, Sum
from CoronaCastilla.models import Factura
from CoronaCastilla.forms import facturaForm, facturaForm, getFacturas
from django.utils import timezone
from django.contrib import messages
from datetime import datetime
import re
import os
from django.template.loader import render_to_string
from xhtml2pdf import pisa
import openpyxl


def generate_excel(request):
    mes_actual = datetime.now().month
    año_actual = datetime.now().year
    facturas = Factura.objects.filter(fecha_salida__year=año_actual, fecha_ssalida__month=mes_actual)
    
    #crear archivo
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Facturas'
    
    # encabezados
    ws.append(['Número', 'Fecha', 'Cliente', 'Concepto', 'BASE IVA', '% IVA', 'Cuota', 'Total'])

    #añadir datos
    for factura in facturas:
        ws.append([factura.numero_factura, factura.fecha_salida, factura.cliente, factura.habitacion, factura.importe_iva, factura.porcentaje_iva, factura.total_factura])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="facturas_{mes_actual}_{año_actual}.xlsx"'

    wb.save(response)
    return response



def generate_pdf(factura, output_path):
    template = 'pdfFactura.html'
    alojamiento_result = factura.alojamiento_dias * factura.alojamiento_precio
    desayuno_result = factura.desayuno_dias * factura.desayuno_precio
    context = {
        'factura': factura,
        'alojamiento_result': alojamiento_result,
        'desayuno_result': desayuno_result,
    }
    html = render_to_string(template, context)
    
    # Guarda el HTML para depuración
    with open('debug_output.html', 'w') as debug_file:
        debug_file.write(html)
        
    with open(output_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html, dest=pdf_file)

    return pisa_status.err


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
        facturas = Factura.objects.filter(fecha_salida__year=año_actual, fecha_salida__month=mes_actual).order_by('id').values()
    
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
        facturas = Factura.objects.filter(query).order_by('id')
    else:
        facturas = Factura.objects.all().order_by('-id')
        
    total_facturado = facturas.aggregate(Sum('total_factura'))['total_factura__sum'] or 0

    # Extraer el nombre del cliente para cada factura
    for factura in facturas:
        factura.cliente_nombre = extract_name(factura.cliente)

    return render(request, 'facturas.html', {'facturas': facturas, 'form': form, 'total_facturado': total_facturado})


def view_factura_id(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
        
    if request.method == 'POST':
        form = facturaForm(request.POST, instance=factura)
        
        if form.is_valid():
            form.save()
            
            factura_name = f"factura_{str(factura.numero_factura).replace('/', '_')}.pdf"
            external_drive_path = "D:\FACTURAS"
            output_path = os.path.join(external_drive_path, factura_name)
            generate_pdf(factura, output_path)
            
            messages.success(request, "Factura actualizada correctamente.")
            return redirect('facturas')
        else:
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
    if request.method == 'POST':
        form = facturaForm(request.POST)
        if form.is_valid():
            factura = form.save(commit=False)
            # El número de factura se calcula automáticamente en la vista, no se modifica en el formulario
            factura.save()
            
            # Obtener el nombre del archivo PDF y guardarlo
            factura_name = f"factura_{factura.numero_factura.replace('/', '_')}.pdf"
            external_drive_path = "D:\\FACTURAS"
            if not os.path.exists(external_drive_path):
                os.makedirs(external_drive_path)
            output_path = os.path.join(external_drive_path, factura_name)
            
            try:
                generate_pdf(factura, output_path)
            except FileNotFoundError as e:
                print(f"Error al generar el PDF: {e}")
                return render(request, 'crearFactura.html', {'form': form, 'error': f"Error al generar el archivo PDF: {str(e)}"})

            return redirect('facturas')
        else:
            print('Formulario inválido:', form.errors)
    else:
        # Crear un nuevo formulario con el número de factura automáticamente calculado
        form = facturaForm()
        # Obtener el año actual
        year = timezone.now().year
        year_suffix = year % 100

        # Filtrar facturas del año actual y obtener la más reciente
        last_invoice = Factura.objects.filter(numero_factura__endswith=f'/{year_suffix}').order_by('-numero_factura').first()

        if last_invoice:
            # Extraer el número secuencial del último número de factura
            last_number = int(last_invoice.numero_factura.split('/')[0])
            new_number = last_number + 1
        else:
            # Si no hay facturas anteriores, empezar con el número 1
            new_number = 1

        # Establecer el nuevo número de factura en el formulario
        form.fields['numero_factura'].initial = f"{new_number}/{year_suffix}"

    return render(request, 'crearFactura.html', {'form': form})



def delete_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    
    if request.method == 'POST':
        factura.delete()
        return redirect('facturas')  # Redirige a la lista de facturas después de eliminar
    
    # Si no es una solicitud POST, renderiza la página de detalles de factura (o alguna otra vista)
    return render(request, 'gestionarFactura.html', {'factura': factura})

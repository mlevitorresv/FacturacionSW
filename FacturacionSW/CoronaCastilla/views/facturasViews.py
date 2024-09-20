from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.db.models import Q, Sum
from CoronaCastilla.models import Factura, Cliente
from CoronaCastilla.forms import facturaForm, facturaForm, getFacturas
from django.utils import timezone
from django.contrib import messages
from datetime import datetime
import re
import os
from django.template.loader import render_to_string
from xhtml2pdf import pisa
import openpyxl
from io import BytesIO



def generate_excel(request):
    meses_en_espanol = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]
    
    # Construir la ruta del archivo de plantilla
    template_path = os.path.join(os.path.dirname(__file__), '..', '..', 'FACTURAS.xlsx')

    # Verificar que el archivo existe
    if not os.path.exists(template_path):
        return HttpResponse("Error: El archivo de plantilla no se encuentra.", status=404)

    try:
        # Cargar plantilla
        wb = openpyxl.load_workbook(template_path)
    except Exception as e:
        return HttpResponse(f"Error al cargar el archivo de plantilla: {str(e)}", status=500)

    # Hoja activa
    ws = wb.active

    ahora = datetime.now()
    mes_actual = ahora.month
    año_actual = ahora.year
    facturas = Factura.objects.filter(fecha_salida__year=año_actual, fecha_salida__month=mes_actual)

    # Comenzar a rellenar desde la fila 7 (por ejemplo)
    start_row = 7

    # Actualizar información en la hoja de cálculo
    ws["C3"] = f"HOSTELERÍA-EJERCICIO {meses_en_espanol[mes_actual - 1]} {año_actual}"
    for index, factura in enumerate(facturas, start=start_row):
        # Extraer cliente y NIF
        cliente_data = " ".join(factura.cliente.split())
        nif_match = re.search(r'\b\d{8}[A-Z]\b', cliente_data)
        if nif_match:
            nif = nif_match.group(0)
            # El nombre es todo lo que está antes del NIF
            nombre = cliente_data.split(nif)[0].strip()

        # Insertar datos en celdas. Por ejemplo:
        ws[f"A{index}"] = factura.numero_factura
        ws[f"B{index}"] = factura.fecha_salida.strftime('%Y-%m-%d')
        ws[f"C{index}"] = nif 
        ws[f"D{index}"] = nombre
        if factura.desayuno_dias > 0:
            ws[f"E{index}"] = factura.habitacion + ' - Desayunos'
        else:
            ws[f"E{index}"] = factura.habitacion
        ws[f"F{index}"] = factura.base_imponible
        ws[f"G{index}"] = factura.porcentaje_iva

    # Crear un archivo en memoria
    output = BytesIO()
    wb.save(output)
    output.seek(0)

    # Crear nombre de archivo con mes en español
    nombre_archivo = f"facturas_{meses_en_espanol[mes_actual - 1]}_{año_actual}.xlsx"

    # Configurar la respuesta HTTP
    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'

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
    cliente_nombre = request.GET.get('cliente', '')
    
    ahora = datetime.now()
    mes_actual = ahora.month
    año_actual = ahora.year
        
    if filtro == 'mes':
        facturas = Factura.objects.filter(fecha_salida__year=año_actual, fecha_salida__month=mes_actual).order_by('-id')
    
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
        facturas = Factura.objects.filter(query).order_by('-id')
    else:
        facturas = Factura.objects.all().order_by('-id')
        
    if cliente_nombre:
        facturas = facturas.filter(cliente__icontains=cliente_nombre)
        
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
    cliente_id = request.GET.get('cliente_id')
    
    if cliente_id:
        cliente = Cliente.objects.get(id=cliente_id)
        cliente_info = f"{cliente.nombre}\n{cliente.direccion}\n{cliente.codigo_postal}\nNIF: {cliente.nif}"
    else:
        cliente_info = ''
    

    
    if request.method == 'GET':
        form = facturaForm(initial={
            'cliente': cliente_info
        })

    print(f"Valor del cliente en el formulario: {form.initial.get('cliente')}")


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

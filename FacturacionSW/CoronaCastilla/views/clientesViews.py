from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from CoronaCastilla.models import Cliente
from CoronaCastilla.forms import clienteForm


def view_clientes(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
    
    cliente_nombre = request.GET.get('cliente', '')
    
    if cliente_nombre:
        clientes = clientes.filter(nombre__icontains=cliente_nombre)
        
    return render(request, 'clientes.html', {'clientes' : clientes})



def view_cliente_id(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        form = clienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = clienteForm(instance=cliente)
        
    context = {
        'cliente': cliente,
        'form': form
    }
    
    return render(request, 'gestionarCliente.html', context)



def post_cliente(request):
    form = clienteForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            cliente = form.save()
            cliente.save()            
            return redirect('clientes')
        else:
            print("formulario invalido", form.errors)
    
    return render(request, 'crearCliente.html', {'form': form})



def delete_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
    
    return render(request, 'gestionarCliente.html', {'cliente': cliente})
    

# Devolver datos de cliente en formato JSON
def get_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    data = {
        'nombre': cliente.nombre,
        'direccion': cliente.direccion,
        'codigo_postal': cliente.codigo_postal,
        'nif': cliente.nif
    }
    return JsonResponse(data)
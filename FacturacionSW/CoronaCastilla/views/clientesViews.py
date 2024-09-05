from django.shortcuts import render, get_object_or_404, redirect
from CoronaCastilla.models import Cliente



def view_clientes(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
        
    return render(request, 'clientes.html', {'clientes' : clientes})

def view_cliente_id(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    return render(request, 'gestionarCliente.html', cliente)

def delete_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
    
    return render(request, 'gestionarCliente.html', {'cliente': cliente})
    

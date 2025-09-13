from django.shortcuts import redirect, render, get_object_or_404

from tienda.forms import ProductoForm
from .models import Producto, Pedido, Cliente


def home(request):
    # render () Recibe: request, ruta  template, contexto(Diccionario)
    return render(request, "tienda/home.html", {})

def lista_productos(request):
    productos = Producto.objects.all().order_by("nombre")
    return render(request, "tienda/producto/lista_productos.html", {"productos": productos})

def lista_clientes(request):
    clientes = Cliente.objects.all().order_by("nombre")
    return render(request, "tienda/cliente/lista_clientes.html", {"clientes": clientes})

def lista_pedidos(request):
    pedido = Pedido.objects.select_related("cliente").prefetch_related(
        "productos").order_by("-fecha")
    return render(request, "tienda/pedido/lista_pedidos.html", {"pedido": pedido})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "tienda/producto/detalle_producto.html", {"producto": producto})

def detalle_pedido(request, pk):
    pedido = get_object_or_404(Pedido.objects.select_related("cliente")).prefetch_related("productos", pk=pk)
    return render(request, "tienda/detalle_pedido.html", {"pedido": pedido})

def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    pedidos = Cliente.pedidos.select_related("cliente".prefetch_related("productos")).order_by("-fecha")
    return render(request, "tienda/cliente/detalle_cliente.html", {"cliente": cliente, "pedidos": pedidos })


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tienda:lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'tienda/producto/crear_producto.html', {'form': form})

def modificar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('tienda:lista_productos')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'tienda/producto/modificar_producto.html', {'form': form, 'producto': producto})
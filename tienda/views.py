from django.shortcuts import redirect, render, get_object_or_404
from django.db import transaction
from django.db.models import Sum, F
# tienda/views.py
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

from tienda.forms import ClienteForm, ProductoForm, PedidoSimpleForm, PedidoItemFormSet
from tienda.serializers import ProductoSerializer
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
    pedidos = Pedido.objects.annotate(
        total_productos=Sum("items__cantidad"),
        total_precio=Sum(F("items__cantidad") * F("items__precio_unitario"))
    )
    return render(request, "tienda/pedido/lista_pedidos.html", {"pedido": pedidos})

def detalle_pedido(request, pk):
    pedido = get_object_or_404(Pedido.objects.select_related("cliente").prefetch_related("productos"), pk=pk )
    return render(request, "tienda/detalle_pedido.html", {"pedido": pedido})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "tienda/producto/detalle_producto.html", {"producto": producto})

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

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tienda:lista_clientes')
    else:
        form = ClienteForm()
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

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect("tienda:lista_productos")
    return render(request, "tienda/eliminar_producto.html", {"producto": producto})

@transaction.atomic
def crear_pedido_items(request):
    if request.method == "POST":
        pedido_form = PedidoSimpleForm(request.POST)
        if pedido_form.is_valid():
            pedido = pedido_form.save()
            formset = PedidoItemFormSet(request.POST, instance=pedido)
            if formset.is_valid():
                formset.save()
                return redirect("tienda:detalle_pedido", pk=pedido.pk)
        else:
            # Si el pedido no es válido...
            pedido = pedido()
            format = PedidoItemFormSet (request.POST, instance=pedido)
    else:
            pedido_form = PedidoSimpleForm()
            formset = PedidoItemFormSet()
        
    return render (request, "tienda/crear_pedido_items.html", {
            "pedido_form": pedido_form,
            "formset": formset,
        })

@transaction.atomic
def editar_pedido_items (request, pk):
    pedido = get_object_or_404 (Pedido, pk=pk)
    if request.method == "POST":
        pedido_form = PedidoSimpleForm (request.POST, instance=pedido)
        formset = PedidoItemFormSet (request.POST, instance=pedido)
        if pedido_form.is_valid () and formset.is_valid():
            pedido_form.save()
            formset.save()
            return redirect("tienda:detalle_pedido", pk=pedido.pk)
    else:
        pedido_form= PedidoSimpleForm (instance=pedido)
        formset = PedidoItemFormSet (instance=pedido)
            
    return redirect (request, "tienda/editar_pedido_items.html", {
        "pedido": pedido,
        "pedido_form": pedido_form,
        "formset": formset,
    })

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
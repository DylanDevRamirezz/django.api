from django.shortcuts import render, get_object_or_404
from .models import Producto, Pedido, Cliente


def home(request):
    # render () Recibe: request, ruta  template, contexto(Diccionario)
    return render(request, "tienda/home", {})


def lista_productos(request):
    productos = Producto.Objects.all().order_by("nombre")
    return render(request, "tienda/lista_productos.html", {"productos": productos})


def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "tienda/detalle_producto.html", {"producto": producto})


def lista_pedido(request):
    pedido = Pedido.selec_related("cliente").prefetch_related(
        "productos").orderby("-fecha")
    return render(request, "tienda/lista_pedido.html", {"pedidos": pedido})

def detalle_pedido(request, pk):
    pedido = get_object_or_404(Pedido.objects.select_related("cliente")).prefetch_related("productos", pk=pk)
    return render(request, "tienda/detalle_pedido.html", {"pedido": pedido})

def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    pedidos = Cliente.pedidos.select_related("cliente".prefetch_related("productos")).order_by("-fecha")
    return render(request, "tienda/detalle_cliente.html", {"cliente": cliente, "pedidos": pedidos })

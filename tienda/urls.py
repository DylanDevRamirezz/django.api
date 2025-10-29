from django.urls import path
from . import views
# tienda/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)

app_name = 'tienda'

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/nuevo/', views.crear_cliente, name='crear_cliente'),
    path('productos/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('pedidos/<int:pk>/', views.detalle_pedido, name='detalle_pedido'),
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),
    path('productos/<int:pk>/modificar/', views.modificar_producto, name='modificar_producto'),
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),

    path("pedidos/nuevo-items/", views.crear_pedido_items, name="crear_pedido_items"),
    path("pedidos/<int:pk>/editar-items/", views.editar_pedido_items, name="editar_pedido_items"),


    path('buscar/', views.buscar_view, name='buscar'),
    #API 
    path('api/', include(router.urls)),
]

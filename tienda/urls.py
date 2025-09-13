from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('pedidos', views.lista_pedidos, name='lista_pedidos'),
    path('productos/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('pedidos/<int:pk>/', views.detalle_pedido, name='detalle_pedido'),
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),
    path('productos/<int:pk>/modificar/', views.modificar_producto, name='modificar_producto'),
]

from django.contrib import admin

from tienda.models import Producto

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio")
    search_fields = ("nombre", "descripcion")
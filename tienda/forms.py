from django import forms
from .models import Cliente, Producto, Pedido, PedidoItem
from django.forms import inlineformset_factory


class ProductoForm(forms.ModelForm):
    class Meta: 
        model = Producto
        fields = ['nombre','descripcion', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Nombre del producto'
            }),
            'descripcion': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Descripción del producto'
            }),
            'precio': forms.NumberInput(attrs={
                'step': '0.01',
                'min': 0,
                'placeholder': 'Precio del producto'
            })
        }

class ClienteForm(forms.ModelForm):
    class Meta: 
        model = Cliente
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Nombre del Cliente'
            }),
            'correo': forms.TextInput(attrs={
                'placeholder': 'Correo electronico del Cliente'
            }),
        }

class PedidoSimpleForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'estado']

class pedidoItemForm(forms.ModelForm):
    class Meta:
        model = PedidoItem
        fields = ['producto', 'cantidad', 'precio_unitario']
        widgest = {
            "cantidad": forms.NumberInput(attrs={
                "min": 1,
                "step": "1"
            }),
            "precio_unitario": forms.NumberInput(attrs={
                "step": "0.01",
                "min": 0
            })
        }

PedidoItemFormSet = inlineformset_factory(
    parent_model=Pedido,
    model=PedidoItem,
    form=pedidoItemForm,
    extra=1,
    can_delete=True
)

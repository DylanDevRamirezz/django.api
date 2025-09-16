from django import forms
from .models import Cliente, Producto

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
        fields = ['nombre','descripcion', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Nombre del Cliente'
            }),
            'correo': forms.TextInput(attrs={
                'placeholder': 'Correo electronico del Cliente'
            }),
        }
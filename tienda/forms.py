from django import forms
from .models import Producto

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
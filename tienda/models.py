from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class TipoUsuario(models.TextChoices):
    SA = 'SA', _('Administrador')
    CLIENTE = 'CLIENTE', _('Cliente')
    TIENDA = 'TIENDA', _('Tienda')

class Credencial(models.Model):
    ultimoAcceso = models.DateField(auto_now_add=True)
    fechaCreacion = models.DateField(auto_now_add=True)
    password = models.CharField(max_length=64, null=False)
    # usuario = models.ForeignKey(Usuario, related_name='usuario', on_delete=models.PROTECT)


class Usuario(models.Model):
    codigo = models.CharField(max_length=10, unique=True, null=False)
    nombre1 = models.CharField(max_length=64, null=False)
    nombre2 = models.CharField(max_length=64, null=True)
    apellido1 = models.CharField(max_length=64, null=False)
    apellido2 = models.CharField(max_length=64, null=True)
    nombreCompleto = models.CharField(
        max_length=124, default=f"{nombre1} {nombre2} {apellido1} {apellido2}", null=False)
    correo = models.EmailField(unique=True)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    credenciales    = models.ManyToManyField(Credencial, related_name='credenciales', blank=True)

    tipo = models.CharField(
        max_length=10,
        choices=TipoUsuario.choices,
        default=TipoUsuario.CLIENTE,
        null=False
    )


class Tienda(models.Model):
    codigo = models.CharField(max_length=16, unique=True, null=False)
    nombreComercial = models.CharField(max_length=124, null=False)
    descripcion = models.TextField()
    administrador = models.ForeignKey(Usuario, related_name='admin', on_delete=models.PROTECT)
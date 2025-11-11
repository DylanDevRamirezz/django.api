from django.core.management.base import BaseCommand
from tienda.models import Producto

class Command(BaseCommand):
    help = "Crea 100 productos de prueba"

    def handle(self, *args, **options):
        productos = [
 Producto(nombre="Smartphone Galaxy S22", descripcion="Celular inteligente 128GB, pantalla AMOLED, cámara triple.", precio=2699.99),
    Producto(nombre="Laptop Dell Inspiron 14", descripcion="Intel i5, 8GB RAM, SSD 256GB, ideal para oficina y estudio.", precio=2499.00),
    Producto(nombre="Auriculares Bluetooth Sony WH-1000XM4", descripcion="Cancelación de ruido, batería de 30 horas.", precio=999.99),
    Producto(nombre="Tablet iPad Air", descripcion="Pantalla de 10.5 pulgadas, chip A14, WiFi y 4G LTE.", precio=1999.00),
    Producto(nombre="Smartwatch Xiaomi Mi Band 7", descripcion="Monitor de actividad física, resistente al agua.", precio=299.00),
    Producto(nombre="Monitor LG 24 pulgadas Full HD", descripcion="Panel IPS, conexiones HDMI y VGA.", precio=799.00),
    Producto(nombre="Teclado mecánico Logitech G413", descripcion="RGB, switches mecánicos, anti-ghosting.", precio=349.99),
    Producto(nombre="Mouse inalámbrico HP X200", descripcion="Sensor óptico de alta precisión.", precio=89.99),
    Producto(nombre="Disco externo Toshiba 1TB", descripcion="USB 3.0, compatible con Windows y Mac.", precio=312.00),
    Producto(nombre="Impresora Epson EcoTank L3150", descripcion="Tanque de tinta, WiFi, impresión móvil.", precio=999.00),
    Producto(nombre="Router TP-Link Archer C6", descripcion="WiFi dual band, 1200Mbps, 4 antenas.", precio=215.00),
    Producto(nombre="Cámara GoPro Hero 9", descripcion="Video 5K, fotos 20MP, sumergible y resistente.", precio=1599.00),
    Producto(nombre="Micro SD Samsung 128GB", descripcion="Clase 10, UHS-I, velocidad gran transferencia.", precio=79.99),
    Producto(nombre="Cargador inalámbrico Anker 10W", descripcion="Fast Charge, compatible con varios dispositivos.", precio=89.90),
    Producto(nombre="Tarjeta de video Nvidia RTX 3060", descripcion="12GB GDDR6, ray tracing, gaming profesional.", precio=2050.00),
    Producto(nombre="Altavoz inteligente Google Nest", descripcion="Control por voz, integración domótica.", precio=399.00),
    Producto(nombre="Webcam Logitech C920 HD Pro", descripcion="Full HD, micrófono integrado, ideal para videollamadas.", precio=279.00),
    Producto(nombre="Case PC Corsair ATX", descripcion="Ventilación avanzada, panel lateral transparente.", precio=324.00),
    Producto(nombre="Adaptador USB-C a HDMI UGREEN", descripcion="Alta calidad de video, plug & play.", precio=94.90),
    Producto(nombre="Cable USB Lightning Apple", descripcion="1 metro, compatible iPhone y iPad.", precio=59.00),

        ]
        for prod in productos:
            prod.save()
        self.stdout.write(self.style.SUCCESS('¡Se han creado 100 productos!'))

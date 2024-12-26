from django.db import models
import datetime

class Factura(models.Model):
    cliente = models.CharField(max_length=500)
    numero_factura = models.CharField(max_length=255, null=True, blank=True)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    desayuno_cantidad = models.IntegerField()
    desayuno_precio = models.FloatField()
    desayuno2_cantidad = models.IntegerField(null=True, blank=True)
    desayuno2_precio = models.FloatField(null=True, blank=True)
    base_imponible = models.FloatField()
    porcentaje_iva = models.IntegerField()
    importe_iva = models.FloatField()
    total_factura = models.FloatField()
    fecha_creacion = models.DateField(default=datetime.date.today())
    numero_cuenta = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Factura {self.numero_factura} - {self.cliente}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    codigo_postal = models.CharField(max_length=255)
    nif = models.CharField(max_length=255)
    
class Habitacion(models.Model):
    factura = models.ForeignKey('Factura', related_name='habitaciones', on_delete=models.CASCADE)
    tipo_habitacion = models.CharField(max_length=255, choices=[
        ('individual', 'Habitación individual'),
        ('doble', 'Habitación doble'),
        ('triple', 'Habitación triple'),
        ('cuadruple', 'Habitación cuadruple')
    ])
    numero_habitacion = models.IntegerField()
    alojamiento_dias = models.IntegerField()
    alojamiento_precio = models.FloatField()

    def __str__(self):
        return f'{self.tipo_habitacion} - {self.numero_habitacion}'

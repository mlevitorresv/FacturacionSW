from django.db import models

class Factura(models.Model):
    cliente = models.CharField(max_length=500)
    numero_factura = models.CharField(max_length=255)
    habitacion = models.CharField(max_length=255)
    habitacion_numero = models.IntegerField()
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    alojamiento_dias = models.IntegerField()
    desayuno_dias = models.IntegerField()
    alojamiento_precio = models.FloatField()
    desayuno_precio = models.FloatField()
    base_imponible = models.FloatField()
    porcentaje_iva = models.IntegerField()
    importe_iva = models.FloatField()
    total_factura = models.FloatField()

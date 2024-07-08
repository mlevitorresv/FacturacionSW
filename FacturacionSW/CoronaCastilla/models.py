from django.db import models

# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=255)
    precio1 = models.FloatField()
    precio2 = models.FloatField()
    precio3 = models.FloatField()
    precio4 = models.FloatField()
    
class Factura(models.Model):
    cliente = models.CharField(max_length=500)
    numero_factura = models.CharField(max_length=255)
    habitacion = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    habitacion_numero = models.IntegerField()
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    alojamiento_dias = models.IntegerField()
    desayuno_dias = models.IntegerField()
    alojamiento_precio = models.FloatField()
    desayuno_precio = models.FloatField()
    importe = models.FloatField()
    base_imponible = models.FloatField()
    porcentaje_iva = models.IntegerField()
    importe_iva = models.FloatField()
    total_factura = models.FloatField()
    
    
    
    
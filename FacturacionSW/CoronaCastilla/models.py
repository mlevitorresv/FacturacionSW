from django.db import models
class Articulo(models.Model):
    CATEGORIAS = [
        ('alojamiento', 'Alojamiento'),
        ('desayuno', 'Desayuno'),
    ]

    nombre = models.CharField(max_length=255)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    precio1 = models.FloatField()
    precio2 = models.FloatField()
    precio3 = models.FloatField()
    precio4 = models.FloatField()

    def __str__(self):
        return self.nombre
    
    

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
    importe = models.FloatField()
    base_imponible = models.FloatField()
    porcentaje_iva = models.IntegerField()
    importe_iva = models.FloatField()
    total_factura = models.FloatField()
    
    
    
    
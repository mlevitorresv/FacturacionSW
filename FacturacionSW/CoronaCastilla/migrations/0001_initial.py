# Generated by Django 5.0.1 on 2024-07-08 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('precio1', models.FloatField()),
                ('precio2', models.FloatField()),
                ('precio3', models.FloatField()),
                ('precio4', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=500)),
                ('numero_factura', models.CharField(max_length=255)),
                ('habitacion_numero', models.IntegerField()),
                ('fecha_entrada', models.DateField()),
                ('fecha_salida', models.DateField()),
                ('alojamiento_dias', models.IntegerField()),
                ('desayuno_dias', models.IntegerField()),
                ('alojamiento_precio', models.FloatField()),
                ('desayuno_precio', models.FloatField()),
                ('importe', models.FloatField()),
                ('base_imponible', models.FloatField()),
                ('porcentaje_iva', models.IntegerField()),
                ('importe_iva', models.FloatField()),
                ('total_factura', models.FloatField()),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CoronaCastilla.articulo')),
            ],
        ),
    ]

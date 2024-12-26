# Generated by Django 5.1.2 on 2024-12-26 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoronaCastilla', '0008_alter_factura_desayuno_precio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitacion',
            name='alojamiento_dias',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha_creacion',
            field=models.DateField(default=datetime.date(2024, 12, 26)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='numero_factura',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

# Generated by Django 5.0.1 on 2024-10-09 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoronaCastilla', '0007_remove_factura_desayuno_dias_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='desayuno_precio',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='numero_factura',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

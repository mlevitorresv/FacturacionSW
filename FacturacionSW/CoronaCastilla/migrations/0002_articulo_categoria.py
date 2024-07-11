# Generated by Django 5.0.1 on 2024-07-11 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoronaCastilla', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='categoria',
            field=models.CharField(choices=[('alojamiento', 'Alojamiento'), ('desayuno', 'Desayuno')], default='alojamiento', max_length=20),
            preserve_default=False,
        ),
    ]

from django import forms
from CoronaCastilla.models import Factura, Cliente, Habitacion
from django.shortcuts import get_object_or_404

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = [
            'cliente', 'numero_factura', 'fecha_entrada', 'fecha_salida', 'desayuno_precio', 
            'base_imponible', 'porcentaje_iva', 'importe_iva', 'total_factura', 'numero_cuenta'
        ]
        widgets = {
            'cliente': forms.Textarea(attrs={'class': 'plantilla__form__basico__area', 'rows': '8', 'id': 'clienteDetails'}),
            'numero_factura': forms.TextInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'numero'}),
            'fecha_entrada': forms.DateInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'fechaEntrada', 'type': 'date', 'id': 'fechaEntrada', 'onchange': 'precioAlojamiento()'}),
            'fecha_salida': forms.DateInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'fechaSalida', 'type': 'date', 'id': 'fechaSalida', 'onchange': 'precioAlojamiento()'}),
            'desayuno_precio': forms.NumberInput(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'precioDesayuno', 'id': 'desayunoPrecio', 'onchange': 'showResults()'}),
            'base_imponible': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'baseImponible', 'id': 'baseImponible'}),
            'porcentaje_iva': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'porcentajeIva', 'value': 10, 'id': 'porcentajeIva', 'onchange': 'showResults()'}),
            'importe_iva': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'importeIva', 'id': 'importeIva'}),
            'total_factura': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'totalFactura', 'id': 'totalFactura'}),
            'numero_cuenta': forms.Textarea(attrs={'class': 'plantilla__form__basico__area', 'rows': '1', 'id': 'numero_cuenta'}),
        }
        
class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['tipo_habitacion', 'numero_habitacion', 'alojamiento_precio']
        widgets = {
            'tipo_habitacion': forms.Select(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'id': 'tipoHabitacion'}),
            'numero_habitacion': forms.NumberInput(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'numeroHabitacion'}),
            'alojamiento_precio': forms.NumberInput(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'precioAlojamiento', 'id': 'alojamientoPrecio_0',  'onchange': 'precioAlojamiento()'}),
        }

HabitacionFormSet = forms.modelformset_factory(
    Habitacion,
    form=HabitacionForm,
    extra=1,
    can_delete=True
)

class clienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre', 'direccion', 'codigo_postal', 'nif'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'nombre'}),
            'direccion': forms.TextInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'direccion'}),
            'codigoPostal': forms.TextInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'codigoPostal'}),
            'nif': forms.TextInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'nif'})
        }
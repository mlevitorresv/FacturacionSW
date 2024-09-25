from django import forms
from CoronaCastilla.models import Factura, Cliente
from django.shortcuts import get_object_or_404

class facturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = [
            'cliente', 'numero_factura', 'habitacion_numero', 'fecha_entrada', 'fecha_salida',
            'alojamiento_dias', 'desayuno_dias', 'alojamiento_precio', 'desayuno_precio', 
            'base_imponible', 'porcentaje_iva', 'importe_iva', 'total_factura', 'habitacion', 'numero_cuenta'
        ]
        widgets = {
            'cliente': forms.Textarea(attrs={'class': 'plantilla__form__basico__area', 'rows': '8', 'id': 'clienteDetails'}),
            'numero_factura': forms.TextInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'numero'}),
            'habitacion_numero': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'numeroHabitacion'}),
            'fecha_entrada': forms.DateInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'fechaEntrada', 'type': 'date'}),
            'fecha_salida': forms.DateInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'fechaSalida', 'type': 'date'}),
            'alojamiento_dias': forms.NumberInput(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'numeroDias', 'id': 'alojamientoDias', 'onchange': 'precioAlojamiento()'}),
            'desayuno_dias': forms.NumberInput(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'numeroDias', 'id': 'desayunoDias', 'onchange': 'precioDesayuno()'}),
            'alojamiento_precio': forms.NumberInput(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'precioAlojamiento', 'id': 'alojamientoPrecio', 'onchange': 'precioAlojamiento()'}),
            'desayuno_precio': forms.NumberInput(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'precioDesayuno', 'id': 'desayunoPrecio', 'onchange': 'precioDesayuno()'}),
            'base_imponible': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'baseImponible', 'id': 'baseImponible'}),
            'porcentaje_iva': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'porcentajeIva', 'value': 10, 'id': 'porcentajeIva', 'onchange': 'showResults()'}),
            'importe_iva': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'importeIva', 'id': 'importeIva'}),
            'total_factura': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'totalFactura', 'id': 'totalFactura'}),
            'numero_cuenta': forms.Textarea(attrs={'class': 'plantilla__form__basico__area', 'rows': '1', 'id': 'numero_cuenta', 'required': 'False'}),
        }

    habitacion = forms.ChoiceField(
        choices=[
            ('habitación individual', 'Habitación individual'),
            ('habitación doble', 'Habitación doble'),
            ('habitación triple', 'Habitación triple'),
            ('habitación cuadruple', 'Habitación cuadruple')
        ],
        widget=forms.Select(attrs={'class': 'plantilla__form__articulos__inputs__input', 'id': 'tipoHabitacion'})
    )
    
class getFacturas(forms.Form):
    uno = forms.BooleanField(required=False, label='Enero')
    dos = forms.BooleanField(required=False, label='Febrero')
    tres = forms.BooleanField(required=False, label='Marzo')
    cuatro = forms.BooleanField(required=False, label='Abril')
    cinco = forms.BooleanField(required=False, label='Mayo')
    seis = forms.BooleanField(required=False, label='Junio')
    siete = forms.BooleanField(required=False, label='Julio')
    ocho = forms.BooleanField(required=False, label='Agosto')
    nueve = forms.BooleanField(required=False, label='Septiembre')
    diez = forms.BooleanField(required=False, label='Octubre')
    once = forms.BooleanField(required=False, label='Noviembre')
    doce = forms.BooleanField(required=False, label='Diciembre')
    
    año = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'main__buttons__find__create', 'placeholder': 'Año'}), label='Año', required=True)
    
    def get_selected_months(self):
        selected_months = []
        for i, month in enumerate(self.fields, start=1):
            if self.cleaned_data.get(month):
                selected_months.append(i)
        return selected_months
    
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
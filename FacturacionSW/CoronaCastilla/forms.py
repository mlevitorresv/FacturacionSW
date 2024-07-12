from django import forms
from CoronaCastilla.models import Factura, Articulo

# forms.py

class facturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = [
            'cliente', 'numero_factura', 'habitacion', 'habitacion_numero', 'fecha_entrada', 'fecha_salida',
            'alojamiento_dias', 'desayuno_dias', 'alojamiento_precio', 'desayuno_precio', 'importe', 'base_imponible', 'porcentaje_iva', 'importe_iva', 'total_factura'
        ]
        widgets = {
            'cliente': forms.Textarea(attrs={'class': 'plantilla__form__basico__area', 'rows': '8'}),
            'numero_factura': forms.TextInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'numero'}),
            'habitacion': forms.Select(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'tipoHabitacion', 'id': 'tipoHabitacion'}),
            'habitacion_numero': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'numeroHabitacion'}),
            'fecha_entrada': forms.DateInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'fechaEntrada', 'type': 'date'}),
            'fecha_salida': forms.DateInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'fechaSalida', 'type': 'date'}),
            'alojamiento_dias': forms.NumberInput(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'numeroDias', 'id': 'alojamientoDias', 'onchange': 'precioAlojamiento()'}),
            'desayuno_dias': forms.NumberInput(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'numeroDias', 'id': 'desayunoDias', 'onchange': 'precioDesayuno()'}),
            'importe': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'importe'}),
            'base_imponible': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'baseImponible', 'disabled': True, 'id': 'baseImponible'}),
            'porcentaje_iva': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'porcentajeIva', 'value': 10, 'id': 'porcentajeIva', 'onchange': 'showResults()'}),
            'importe_iva': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'importeIva', 'disabled': True, 'id': 'importeIva'}),
            'total_factura': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'totalFactura', 'disabled': True, 'id': 'totalFactura'})
        }

    alojamiento_precio = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'precioHabitacion', 'id': 'alojamientoPrecio'})
    )

    desayuno_precio = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'precioDesayuno', 'id': 'desayunoPrecio'})
    )


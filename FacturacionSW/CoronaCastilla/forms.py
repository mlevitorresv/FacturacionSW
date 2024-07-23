from django import forms
from CoronaCastilla.models import Factura, Articulo
from django.shortcuts import get_object_or_404

class facturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = [
            'cliente', 'numero_factura', 'habitacion_numero', 'fecha_entrada', 'fecha_salida',
            'alojamiento_dias', 'desayuno_dias', 'alojamiento_precio', 'desayuno_precio', 'base_imponible', 'porcentaje_iva', 'importe_iva', 'total_factura'
        ]
        widgets = {
            'cliente': forms.Textarea(attrs={'class': 'plantilla__form__basico__area', 'rows': '8'}),
            'numero_factura': forms.TextInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'numero'}),
            'habitacion_numero': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'numeroHabitacion'}),
            'fecha_entrada': forms.DateInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'fechaEntrada', 'type': 'date'}),
            'fecha_salida': forms.DateInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'fechaSalida', 'type': 'date'}),
            'alojamiento_dias': forms.NumberInput(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'numeroDias', 'id': 'alojamientoDias', 'onchange': 'precioAlojamiento()'}),
            'desayuno_dias': forms.NumberInput(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'numeroDias', 'id': 'desayunoDias', 'onchange': 'precioDesayuno()'}),
            'base_imponible': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'baseImponible', 'id': 'baseImponible'}),
            'porcentaje_iva': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'porcentajeIva', 'value': 10, 'id': 'porcentajeIva', 'onchange': 'showResults()'}),
            'importe_iva': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'importeIva', 'id': 'importeIva'}),
            'total_factura': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'totalFactura', 'id': 'totalFactura'})
        }

    alojamiento_precio = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'precioHabitacion', 'id': 'alojamientoPrecio', 'onchange': 'precioAlojamiento()'})
    )

    desayuno_precio = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'precioDesayuno', 'id': 'desayunoPrecio', 'onchange': 'precioDesayuno()'})
    )

    tipoHabitacion = forms.ChoiceField(
        choices=[
            ('habitación individual', 'Habitación individual'),
            ('habitación doble', 'Habitación doble'),
            ('habitación triple', 'Habitación triple'),
            ('habitación cuadruple', 'Habitación cuadruple')
        ],
        widget=forms.Select(attrs={'class': 'plantilla__form__articulos__inputs__input', 'id': 'tipoHabitacion'})
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['alojamiento_precio'].choices = self.get_initial_choices()
        self.fields['desayuno_precio'].choices = self.get_initial_choices()

    def get_initial_choices(self):
        return []
    
class facturaEditForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = [
            'cliente', 'numero_factura', 'habitacion_numero', 'fecha_entrada', 'fecha_salida',
            'alojamiento_dias', 'desayuno_dias', 'alojamiento_precio', 'desayuno_precio', 'base_imponible', 'porcentaje_iva', 'importe_iva', 'total_factura'
        ]
        widgets = {
            'cliente': forms.Textarea(attrs={'class': 'plantilla__form__basico__area', 'rows': '8'}),
            'numero_factura': forms.TextInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'numero'}),
            'habitacion_numero': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'numeroHabitacion'}),
            'fecha_entrada': forms.DateInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'fechaEntrada', 'type': 'date'}),
            'fecha_salida': forms.DateInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'fechaSalida', 'type': 'date'}),
            'alojamiento_dias': forms.NumberInput(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'numeroDias', 'id': 'alojamientoDias', 'onchange': 'precioAlojamiento()'}),
            'desayuno_dias': forms.NumberInput(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'numeroDias', 'id': 'desayunoDias', 'onchange': 'precioDesayuno()'}),
            'base_imponible': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'baseImponible', 'id': 'baseImponible'}),
            'porcentaje_iva': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'porcentajeIva', 'value': 10, 'id': 'porcentajeIva', 'onchange': 'showResults()'}),
            'importe_iva': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'importeIva', 'id': 'importeIva'}),
            'total_factura': forms.NumberInput(attrs={'class': 'plantilla__form__articulos__inputs__input', 'name': 'totalFactura', 'id': 'totalFactura'})
        }

    alojamiento_precio = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'precioHabitacion', 'id': 'alojamientoPrecio', 'onchange': 'precioAlojamiento()'})
    )

    desayuno_precio = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'plantilla__form__tabla__tbody__trow__tdata__input', 'name': 'precioDesayuno', 'id': 'desayunoPrecio', 'onchange': 'precioDesayuno()'})
    )

    tipoHabitacion = forms.ChoiceField(
        choices=[
            ('habitación individual', 'Habitación individual'),
            ('habitación doble', 'Habitación doble'),
            ('habitación triple', 'Habitación triple'),
            ('habitación cuadruple', 'Habitación cuadruple')
        ],
        widget=forms.Select(attrs={'class': 'plantilla__form__articulos__inputs__input', 'id': 'tipoHabitacion'})
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        instance = kwargs.get('instance')
        if instance:
            self.fields['alojamiento_precio'].choices = self.get_initial_choices(instance.habitacion.nombre)
            self.fields['desayuno_precio'].choices = self.get_initial_choices('desayuno')
            
            self.fields['alojamiento_precio'].initial = str(instance.alojamiento_precio)  # Asegúrate de que esto coincida con el valor en las opciones
            self.fields['desayuno_precio'].initial = str(instance.desayuno_precio) # Asegúrate de que esto coincida con el valor en las opciones
            self.fields['tipoHabitacion'].initial = instance.habitacion.nombre  # Asegúrate de que esto coincida con las opciones disponibles
        else:
            self.fields['alojamiento_precio'].choices = self.get_initial_choices(instance.habitacion.nombre)
            self.fields['desayuno_precio'].choices = self.get_initial_choices('desayuno')
        

    def get_initial_choices(self, tipo):
        articulo = get_object_or_404(Articulo, nombre=tipo)
        return [(str(articulo.precio1), f'€{articulo.precio1}'),(str(articulo.precio2), f'€{articulo.precio2}'),(str(articulo.precio3), f'€{articulo.precio3}'),(str(articulo.precio4), f'€{articulo.precio4}') ]    
    
class articuloEditForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['precio1', 'precio2', 'precio3', 'precio4']
        
        
class getFacturas(forms.Form):
    select_facturas = forms.ChoiceField(
        choices=[
            ('todas', 'todas'),
            ('mes', 'Último mes'),
            ('meses', 'Últimos 3 meses')
        ],
        widget=forms.Select(attrs={'class': 'main__buttons__find__select', 'name': 'select_facturas', 'id': 'select-facturas', 'onchange': 'actualizarFacturas()'})
    )
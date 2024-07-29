const precioAlojamiento = () => {
    dias = document.getElementById('alojamientoDias')
    precio = document.getElementById('alojamientoPrecio')
    result = document.getElementById('alojamientoResult')

    total = dias.value * precio.value
    result.innerHTML = Math.round(total * 100) / 100

    showResults()
}

const precioDesayuno = () => {
    dias = document.getElementById('desayunoDias')
    precio = document.getElementById('desayunoPrecio')
    result = document.getElementById('desayunoResult')

    total = dias.value * precio.value
    result.innerHTML = Math.round(total * 100) / 100
    showResults()
}

const showResults = () => {
    let alojamiento = document.getElementById('alojamientoResult')
    let desayuno = document.getElementById('desayunoResult')

    const ivaInput = document.getElementById('porcentajeIva')
    const importeIvaInput = document.getElementById('importeIva')
    const baseImponibleInput = document.getElementById('baseImponible')
    const totalFacturaInput = document.getElementById('totalFactura')

    alojamiento = parseFloat(alojamiento.innerText || alojamiento.textContent);
    desayuno = parseFloat(desayuno.innerText || desayuno.textContent);

    if (isNaN(alojamiento)) alojamiento = 0;
    if (isNaN(desayuno)) desayuno = 0;

    const precio = alojamiento + desayuno
    const importeIva = Math.round(precio * (ivaInput.value / 100) * 100) / 100
    const baseImponible = Math.round((precio * 100) / 100) - importeIva
    const totalFactura = baseImponible + importeIva



    importeIvaInput.value = importeIva
    baseImponibleInput.value = baseImponible
    totalFacturaInput.value = totalFactura
}



$(document).ready(function () {
    $('#tipoHabitacion').change(function () {
        var tipoHabitacion = $(this).val();
        $.ajax({
            url: '/get-precios/',
            data: {
                'tipoHabitacion': tipoHabitacion
            },
            dataType: 'json',
            success: function (data) {
                $('#alojamientoPrecio').empty();
                for (var key in data) {
                    if (data.hasOwnProperty(key)) {
                        var precio = parseFloat(data[key]).toFixed(1); // Asegurar 2 decimales
                        $('#alojamientoPrecio').append($('<option>', {
                            value: precio,
                            text: '€' + precio
                        }));
                    }
                }
            }
        });
    });
});

$(document).ready(function () {
    $('#desayunoDias').change(function () {
        var tipoHabitacion = 'desayuno';
        $.ajax({
            url: '/get-precios/',
            data: {
                'tipoHabitacion': tipoHabitacion
            },
            dataType: 'json',
            success: function (data) {
                $('#desayunoPrecio').empty();
                for (var key in data) {
                    if (data.hasOwnProperty(key)) {
                        var precio = parseFloat(data[key]).toFixed(1); // Asegurar 2 decimales
                        $('#desayunoPrecio').append($('<option>', {
                            value: precio,
                            text: '€' + precio
                        }));
                    }
                }
            }
        });
    });
});



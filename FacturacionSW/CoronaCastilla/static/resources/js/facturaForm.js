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




document.addEventListener('DOMContentLoaded', function() {
    const clientesSelect = document.getElementById('clientesSelect');
    const clienteDetails = document.getElementById('clienteDetails');

    clientesSelect.addEventListener('change', function() {
        const clienteId = this.value;

        if (clienteId) {
            // Hacer la solicitud AJAX para obtener los datos del cliente
            fetch(`/get_cliente/${clienteId}/`)
                .then(response => response.json())
                .then(data => {
                    console.log("Datos del cliente recibidos:", data); // Debug: Verifica los datos en la consola

                    // Rellenar el textarea con los datos del cliente
                    clienteDetails.value = `
                        ${data.nombre}\t ${data.nif} \n
                        ${data.direccion}\n
                        ${data.codigo_postal}\n
                    `;
                })
                .catch(error => {
                    console.error('Error al obtener los datos del cliente:', error);
                    clienteDetails.value = 'Error al obtener los datos del cliente.';
                });
        } else {
            // Si no hay cliente seleccionado, limpiar el textarea
            clienteDetails.value = '';
        }
    });
});


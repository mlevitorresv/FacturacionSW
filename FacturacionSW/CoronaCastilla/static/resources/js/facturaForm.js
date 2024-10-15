function roundToTwo(num) {
    return num.toFixed(2)
}

const precioAlojamiento = () => {
    const rows = document.querySelectorAll('.plantilla__form__tabla__tbody__trow');  // Seleccionar todas las filas
    const entrada = document.getElementById('fechaEntrada')
    const salida = document.getElementById('fechaSalida')

    console.log('fechas ', entrada.value, salida.value)

    rows.forEach((row, index) => {
        console.log('dentro del for')
        const precio = row.querySelector(`#alojamientoPrecio_${index}`);
        console.log('precio', precio)
        const result = row.querySelector(`#alojamientoResult_${index}`);
        console.log('result', result)

        if (entrada && salida && precio) {
            const fechaEntrada = new Date(entrada.value);
            const fechaSalida = new Date(salida.value);
            console.log('fechas: ', salida, entrada)
            const diferenciaTiempo = fechaSalida - fechaEntrada;
            console.log('dif de tiempo: ', diferenciaTiempo)

            const dias = diferenciaTiempo / (1000 * 60 * 60 * 24);
            console.log('dias', dias)
            const total = dias * precio.value;
            console.log('total', total)

            result.innerHTML = roundToTwo(total);
        }
    });

    showResults();  // Actualizar el resultado total
};


const precioDesayuno = () => {
    precio = document.getElementById('desayunoPrecio')
    result = document.getElementById('desayunoResult')

    result.innerHTML = precio.value
    showResults()
}

const showResults = () => {
    let alojamientoTotal = 0;

    // Sumar todos los resultados de alojamiento
    const alojamientoResults = document.querySelectorAll('[id^="alojamientoResult"]');
    alojamientoResults.forEach((result) => {
        let value = parseFloat(result.innerText || result.textContent);
        if (!isNaN(value)) {
            alojamientoTotal += value;
        }
    });

    let desayuno = parseFloat(document.getElementById('desayunoResult').innerText || 0);

    if (isNaN(desayuno)) desayuno = 0;

    let importeIva = 0;
    let baseImponible = 0;
    let totalFactura = 0;

    const precio = alojamientoTotal + desayuno;
    const ivaInput = document.getElementById('porcentajeIva');

    if (ivaInput.value == 10) {
        baseImponible = roundToTwo(precio / 1.1);
        totalFactura = roundToTwo(precio);
        importeIva = roundToTwo(totalFactura - baseImponible);
    } else {
        importeIva = roundToTwo(precio * (ivaInput.value / 100));
        baseImponible = roundToTwo(precio - importeIva);
        totalFactura = roundToTwo(baseImponible + importeIva);
    }

    document.getElementById('importeIva').value = importeIva;
    document.getElementById('baseImponible').value = baseImponible;
    document.getElementById('totalFactura').value = totalFactura;
};



const tbody = document.querySelector('.plantilla__form__tabla__tbody');
let formCount = document.querySelectorAll('.plantilla__form__tabla__tbody__trow').length;

const showFields = () => {
    let fields = document.getElementById('alojamientoClonar');
    let clon = fields.cloneNode(true);  // Clonar la fila

    clon.id = `form-${formCount}`;  // Asignar un nuevo ID único al clon

    // Seleccionar todos los inputs y selects del clon
    const inputs = clon.querySelectorAll('input, select');
    inputs.forEach((input) => {
        const name = input.name;
        if (name) {
            input.name = name.replace('__prefix__', formCount);  // Reemplazar __prefix__ por el formCount actual
            input.id = `id_${input.name}`;  // Actualizar el id también
        }
        input.value = '';  // Limpiar el valor del campo clonado
    });

    // Asignar nuevos IDs para las fechas y precio
    clon.querySelector('input[name$="alojamiento_precio"]').id = `alojamientoPrecio_${formCount}`;
    clon.querySelector('td[id$="alojamientoResult"]').id = `alojamientoResult_${formCount}`;

    tbody.appendChild(clon);  // Añadir el clon al tbody
    formCount++;  // Incrementar el contador de formularios
    console.log("creado form nuevo:", clon)

    // Actualizar el valor de TOTAL_FORMS en el formset
    document.getElementById('id_form-TOTAL_FORMS').value = formCount;
};



const printSave = () => {
    form = document.getElementById('facturaForm')
    form.submit()
    print()
}
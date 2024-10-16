function roundToTwo(num) {
    return num.toFixed(2)
}

const precioAlojamiento = () => {
    const rows = document.querySelectorAll('.plantilla__form__tabla__tbody__trow');  // Seleccionar todas las filas
    const entrada = document.getElementById('fechaEntrada');
    const salida = document.getElementById('fechaSalida');

    if (!entrada || !salida) return;


    const fechaEntrada = new Date(entrada.value);
    const fechaSalida = new Date(salida.value);
    const diferenciaTiempo = fechaSalida - fechaEntrada;
    const dias = diferenciaTiempo / (1000 * 60 * 60 * 24);


    rows.forEach((row, index) => {
        
        // Modificación para seleccionar correctamente los inputs sin depender del índice en el ID
        const precioInput = row.querySelector('input[name$="alojamiento_precio"]');
        const resultCell = row.querySelector('td[id^="alojamientoResult"]');
        
        if (precioInput && resultCell) {            
            const precioPorNoche = parseFloat(precioInput.value) || 0;
            const total = dias * precioPorNoche;
            
            resultCell.innerHTML = roundToTwo(total);
        }
    });

    showResults();  // Actualizar el resultado total
};



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
    console.log("alojamientoTotal: ", alojamientoTotal)
    let desayuno = parseFloat(document.getElementById('desayunoPrecio').value);
    console.log("desayuno: ", desayuno)


    let importeIva = 0;
    let baseImponible = 0;
    let totalFactura = 0;

    const precio = alojamientoTotal + desayuno;
    const ivaInput = document.getElementById('porcentajeIva');
    console.log('total: ', precio)
    if (ivaInput.value == 10) {
        baseImponible = roundToTwo(precio / 1.1);
        totalFactura = roundToTwo(precio);
        importeIva = roundToTwo(totalFactura - baseImponible);
    } else {
        importeIva = roundToTwo(precio * (ivaInput.value / 100));
        baseImponible = roundToTwo(precio - importeIva);
        totalFactura = roundToTwo(baseImponible + importeIva);
    }
    console.log(`importeIva ${importeIva}, baseImponible ${baseImponible}, totalFctura ${totalFactura}`)
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

    const alojamientoResult = clon.querySelector('td[id$="alojamientoResult_0"]');
    
    if (alojamientoResult) {
        // Asignar un nuevo ID único para este clon
        alojamientoResult.id = `alojamientoResult_${formCount}`;
    } else {
        console.error('No se encontró el elemento con id que termina en "alojamientoResult". Verifica el HTML.');
    }

    tbody.appendChild(clon);  // Añadir el clon al tbody
    formCount++;  // Incrementar el contador de formularios
    console.log("creado form nuevo:", clon);

    // Actualizar el valor de TOTAL_FORMS en el formset
    document.getElementById('id_form-TOTAL_FORMS').value = formCount;
};



const printSave = () => {
    form = document.getElementById('facturaForm')
    form.submit()
    print()
}
function roundToTwo(num) {
    return +(Math.round(num + "e+2") + "e-2");
}

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

    let importeIva = 0;
    let baseImponible = 0;
    let totalFactura = 0;

    const precio = alojamiento + desayuno
    if (ivaInput.value == 10) {
        baseImponible = roundToTwo(precio / 1.1)
        totalFactura = roundToTwo(alojamiento + desayuno)
        importeIva = roundToTwo(totalFactura - baseImponible)
    } else {
        importeIva = roundToTwo(precio * (ivaInput.value / 100) * 100) / 100
        baseImponible = roundToTwo((precio * 100) / 100) - importeIva
        totalFactura = baseImponible + importeIva
    }
    importeIvaInput.value = importeIva
    baseImponibleInput.value = baseImponible
    totalFacturaInput.value = totalFactura
}


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

    tbody.appendChild(clon);  // Añadir el clon al tbody
    formCount++;  // Incrementar el contador de formularios

    // Actualizar el valor de TOTAL_FORMS en el formset
    document.getElementById('id_form-TOTAL_FORMS').value = formCount;  // Asegúrate de que esto esté en el FormSet
};

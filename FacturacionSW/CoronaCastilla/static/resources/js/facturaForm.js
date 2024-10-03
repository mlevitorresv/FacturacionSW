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

const showFields = (n) => {
    tbody.innerHTML = ''
    for (let i = 0; i < n; i++) {

        const newRow = document.createElement('tr')
        newRow.classList.add('plantilla__form__tabla__tbody__trow')

        newRow.innerHTML = `
            <td class="plantilla__form__tabla__tbody__trow__tdata">ALOJAMIENTO</td>
            <td class="plantilla__form__tabla__tbody__trow__tdata">
                <input type="text" name="habitacion_tipo_${i + 1}" placeholder="Tipo Habitación">
            </td>
            <td class="plantilla__form__tabla__tbody__trow__tdata">
                <input type="number" name="habitacion_numero_${i + 1}" placeholder="Número Habitación">
            </td>
            <td class="plantilla__form__tabla__tbody__trow__tdata">
                <input type="number" name="dias_${i + 1}" placeholder="Días">
            </td>
            <td class="plantilla__form__tabla__tbody__trow__tdata">
                <input type="number" step="0.01" name="precio_${i + 1}" placeholder="Euros">
            </td>
            <td class="plantilla__form__tabla__tbody__trow__tdata">
                <span id="importe_${i + 1}"></span>
            </td>
        `

        tbody.appendChild(newRow)
    }
}
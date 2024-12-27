function roundToTwo(num) {
    return num.toFixed(2)
}

const precioAlojamiento = () => {
    const rows = document.querySelectorAll('.plantilla__form__tabla__tbody__trow');  // Seleccionar todas las filas

    rows.forEach((row, index) => {

        // Modificación para seleccionar correctamente los inputs sin depender del índice en el ID
        const precioInput = row.querySelector('input[name$="alojamiento_precio"]');
        const diasInput = row.querySelector('input[name$="alojamiento_dias"]');
        const resultCell = row.querySelector('td[id^="alojamientoResult"]');

        if (precioInput && resultCell) {
            const precioPorNoche = parseFloat(precioInput.value) || 0;
            const total = diasInput.value * precioPorNoche;

            resultCell.innerHTML = roundToTwo(total);
        }
    });

    showResults();  // Actualizar el resultado total
};


const precioDesayunos = () => {
    const cantidad1 = document.getElementById("desayunoCantidad")
    const precio1 = document.getElementById("desayunoPrecio")
    const cantidad2 = document.getElementById("desayunoCantidad2")
    const precio2 = document.getElementById("desayunoPrecio2")

    const total1input = document.getElementById("desayunoTotal")
    const total2input = document.getElementById("desayuno2Total")

    total1input.innerHTML = roundToTwo(parseFloat(cantidad1.value + precio1.value))
    total2input.innerHTML = roundToTwo(parseFloat(cantidad2.value + precio2.value))
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
    console.log(`importeIva ${importeIva}, baseImponible ${baseImponible}, totalFactura ${totalFactura}`)
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
            input.name = name.replace(/habitaciones-\d+/, `habitaciones-${formCount}`);  // Reemplazar el índice en el name
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
    document.getElementById('id_habitaciones-TOTAL_FORMS').value = formCount;
};


window.onload = function () {
    precioAlojamiento()
    precioDesayunos()
}


const deleteCheckboxes = $("input[type='checkbox'][name*='DELETE']");
deleteCheckboxes.on("change", async function (event) {
    event.preventDefault();  // Evitar el comportamiento predeterminado
    const urlCompleta = window.location.href;

    const form = document.getElementById("editForm");

    // Enviar el formulario y esperar a que se procese antes de redirigir
    try {
        const response = await fetch(form.action, {
            method: form.method,
            body: new FormData(form)
        });

        // Redirigir solo si la respuesta es exitosa
        if (response.ok) {
            window.location.href = urlCompleta;
        } else {
            console.error("Hubo un problema al enviar el formulario:", response.status);
        }
    } catch (error) {
        console.error("Error al enviar el formulario:", error);
    }
});



const cerrarNueva = async () => {
    const form = document.getElementById('facturaForm');

    if (!form) {
        alert("Formulario no encontrado");
        return;
    }

    try {
        // Enviar datos del formulario al backend
        const response = await fetch('http://localhost:8000/facturas/cerrar/', {
            method: form.method || 'POST', // Asegura que haya un método definido
            body: new FormData(form)
        });

        await print()
        window.location.href = 'http://localhost:8000/facturas'
    } catch (error) {
        console.error("Error al enviar el formulario", error);
    }
};

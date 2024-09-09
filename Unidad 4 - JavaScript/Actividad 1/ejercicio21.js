let suma = 0;
let nro;

do {
	nro = prompt('Escriba un número:');

	if (nro === null) {
		break;
	}

	nro = Number(nro);

	if (isNaN(nro)) {
		alert('El dato ingresado no es un número. Vuelva a ingresar.');
	} else {
		suma += nro;
	}
} while (true);

document.write('Suma = ' + suma);

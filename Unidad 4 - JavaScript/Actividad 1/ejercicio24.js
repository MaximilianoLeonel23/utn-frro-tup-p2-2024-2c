const nro = Number(prompt('Escriba un número'));

for (let i = nro; i >= 1; i--) {
	let cadena = '';
	for (let k = 1; k <= i; k++) {
		cadena += String(i);
	}
	document.write(`<p>${cadena}</p>`);
}

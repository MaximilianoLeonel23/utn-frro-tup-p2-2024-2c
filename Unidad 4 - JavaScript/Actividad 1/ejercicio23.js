for (let i = 1; i <= 30; i++) {
	let cadena = '';
	for (let k = 1; k <= i; k++) {
		cadena += String(i);
	}
	document.write(`<p>${cadena}</p>`);
}

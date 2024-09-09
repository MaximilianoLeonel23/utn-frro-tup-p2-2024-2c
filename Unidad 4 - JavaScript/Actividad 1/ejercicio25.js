for (let i = 1; i <= 500; i++) {
	let esMultiplo = '';
	if (i % 4 === 0) {
		esMultiplo = '(Múltiplo de 4)';
	} else if (i % 9 === 0) esMultiplo = '(Múltiplo de 9';

	document.write(`<p>${i} ${esMultiplo != '' ? esMultiplo : ''}</p>`);
	if (i % 5 === 0) {
		document.write("<div class='divisor'></div>");
	}
	esMultiplo = '';
}

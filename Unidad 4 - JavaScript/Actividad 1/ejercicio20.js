let cadena = prompt('Escriba una cadena de texto: ');
let cadenasConcat = cadena;
while (cadena != null) {
	cadena = prompt('Escriba otra cadena de texto: ');
	if (cadena != null) {
		cadenasConcat += ' - ' + cadena;
	}
}
document.write(cadenasConcat);

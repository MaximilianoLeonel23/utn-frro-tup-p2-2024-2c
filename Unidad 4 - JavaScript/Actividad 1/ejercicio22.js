/* 
Realizar una página con un script que calculeel valor de la letra de un número
 de DNI (Documento Nacional de Identidad).
 El algoritmo para calcular la letra del dni es elsiguiente :
 ● El número debe ser entre 0 y 99999999
 ● Debemos calcular el resto de la división entera entreel número y el número
 23.
 ● Según el resultado, de 0 a 22, le corresponderá unaletra de las siguientes:
 (T, R, W, A, G, M, Y, F, P, D, X, B, N, J, Z, S, Q,V, H, L, C, K, E)
 ● Si lo introducido no es un número deberá indicarsecon un alert y volver a
 preguntar.
 ● Deberá de repetirse el proceso hasta que el usuariopulse «cancelar».
*/
let nro;
const letras = [
	'T',
	'R',
	'W',
	'A',
	'G',
	'M',
	'Y',
	'F',
	'P',
	'D',
	'X',
	'B',
	'N',
	'J',
	'Z',
	'S',
	'Q',
	'V',
	'H',
	'L',
	'C',
	'K',
	'E',
];
do {
	nro = prompt('Escriba un número:');
	let resto;

	if (nro === null) {
		break;
	}

	nro = Number(nro);

	if (isNaN(nro)) {
		alert('Ingrese un número válido');
	} else {
		if (nro > 0 && nro < 99999999) {
			resto = nro % 23;

			console.log(`El DNI ${nro} equivale a la letra ${letras[resto]}`);
		} else {
			alert('Ingrese un número entre 0 y 99999999');
		}
	}
} while (true);

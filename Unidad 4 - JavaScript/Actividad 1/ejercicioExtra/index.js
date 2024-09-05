const nombre = prompt('Escriba su nombre: ');
const valor1 = Number(prompt('Valor 1: '));
const valor2 = Number(prompt('Valor 2: '));

const suma = valor1 + valor2;
const resta = valor1 - valor2;
const producto = valor1 * valor2;
const cociente = valor1 / valor2;

document.write(`
	<main>
		<div class='contenedor'>
			<h1 class='nombre'>Hola ${nombre}</h1>
			<h2 class='encabezado_operaciones'>Operaciones Aritméticas</h2>
			<div class='lista_operaciones'>
                <p class='operacion'>Suma = ${valor1} + ${valor2} = ${suma}</p>
                <p class='operacion'>Resta = ${valor1} - ${valor2} = ${resta}</p>
                <p class='operacion'>Producto = ${valor1} * ${valor2} = ${producto}</p>
                <p class='operacion'>Cociente = ${valor1} / ${valor2} = ${cociente}</p>
			</div>
		</div>
	</main>`);

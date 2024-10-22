class Alumno:
    def __init__(self, nombre, nota):
        self.set_nombre(nombre)
        self.set_nota(nota)
    def get_nombre(self):
        return self.nombre
    def get_nota(self):
        return self.nota
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_nota(self, nota):
        self.nota = nota
   
    def mostrar_resultado(self):
        print(f"La nota es: {self.get_nota()}. {"Aprobado" if self.get_nota() >= 6 else "Desaprobado"}")

alumno1 = Alumno("Matias", 4)
alumno2 = Alumno("Santiago", 8)

alumno1.mostrar_resultado()
alumno2.mostrar_resultado()
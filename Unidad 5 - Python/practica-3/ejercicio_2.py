class Persona:
    def __init__(self, nombre, edad):
        self.set_nombre(nombre)
        self.set_edad(edad)
    
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_edad(self, edad):
        self.edad = edad
    def imprimir(self):
        print(f"{self.get_nombre()} tiene {self.get_edad()} años");

persona1 = Persona("Lautaro", 26)
persona2 = Persona("Delfina", 24)
persona1.imprimir()
persona2.imprimir()
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
    def es_mayor_de_edad(self):
        return self.get_edad() >= 15
    def imprimir(self):
        print(f"{self.get_nombre()} tiene {self.get_edad()} años");


persona1 = Persona("Lautaro", 26)
persona2 = Persona("Delfina", 16)
persona1.imprimir()
persona2.imprimir()
print(persona1.es_mayor_de_edad())
print(persona2.es_mayor_de_edad())
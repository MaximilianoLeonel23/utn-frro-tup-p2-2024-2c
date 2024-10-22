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
    
    def es_mayor_que(self, persona):
        if (self.get_edad() > persona.get_edad()):
            print(self.get_nombre() + " es mayor que " + persona.get_nombre())
        else:
            print(self.get_nombre() + " no es mayor que " + persona.get_nombre())

    def imprimir(self):
        print(f"{self.get_nombre()} tiene {self.get_edad()} años");


persona1 = Persona("Lautaro", 26)
persona2 = Persona("Delfina", 16)


persona1.es_mayor_que(persona2)
persona2.es_mayor_que(persona1)

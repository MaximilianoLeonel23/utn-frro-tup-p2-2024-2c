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

    @staticmethod
    def get_mayor(persona1, persona2):
        if (persona1.get_edad() > persona2.get_edad()):
            return persona1.get_nombre() + " es mayor"
        
        elif (persona2.get_edad() > persona1.get_edad()):
            return persona2.get_nombre() + " es mayor"
        else:
            return "Tienen la misma edad"

    def imprimir(self):
        print(f"{self.get_nombre()} tiene {self.get_edad()} años");


persona1 = Persona("Lautaro", 26)
persona2 = Persona("Delfina", 16)
persona3 = Persona("Sofia", 26)

print(Persona.get_mayor(persona1, persona2))
print(Persona.get_mayor(persona3, persona1))

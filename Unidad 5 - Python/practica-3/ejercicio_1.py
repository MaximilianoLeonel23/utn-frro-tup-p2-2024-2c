class Persona:
   
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

persona1 = Persona()
persona1.set_nombre("Lautaro")
persona1.set_edad(26)
persona2 = Persona()
persona2.set_nombre("Delfina")
persona2.set_edad(24)
persona1.imprimir()
persona2.imprimir()
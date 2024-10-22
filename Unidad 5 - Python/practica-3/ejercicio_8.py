class Calculadora:
    def __init__(self, nro1, nro2):
        self.set_nro1(nro1)
        self.set_nro2(nro2)

    def get_nro1(self):
        return self.nro1 
    def get_nro2(self):
        return self.nro2
    def set_nro1(self, nro):
        self.nro1 = nro
    def set_nro2(self, nro):
        self.nro2 = nro        
    def suma(self):
        return self.get_nro1() + self.get_nro2()
    
    def resta(self):
        return self.get_nro1() - self.get_nro2()
    def multiplicacion(self):
        return self.get_nro1() * self.get_nro2()
    def division(self):
        return self.get_nro1() / self.get_nro2()
    
    def __str__(self):
        return f"{self.get_nro1()} + {self.get_nro2()} = {self.suma()} \n{self.get_nro1()} - {self.get_nro2()} = {self.resta()}\n{self.get_nro1()} * {self.get_nro2()} = {self.multiplicacion()} \n{self.get_nro1()} / {self.get_nro2()} = {self.division()}"
    

nro1 = int(input("Ingrese el primer número"))
nro2 = int(input("Ingrese el segundo número"))


calculadora = Calculadora(nro1, nro2)
print(str(calculadora))
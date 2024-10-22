class Triangulo:
    def __init__(self, lados):
        self.set_lados(lados)

    def get_lados(self):
        return self.lados
        
    def set_lados(self, lados):
        self.lados = lados

    def get_lado_mayor(self):
        return max(self.get_lados())
    
    def get_tipo_triangulo(self):
        lados = self.get_lados()
        if (lados[0] == lados[1] and lados[0] == lados[2]):
            return "equilatero"
        elif (lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]):
            return "isósceles"
        else:
            return "escaleno" 
        
    def __str__(self):
        return f"El triángulo es de tipo {self.get_tipo_triangulo()}, y su lado mayor mide {self.get_lado_mayor()}"

triangulo_1 = Triangulo([5, 6, 6])
triangulo_2 = Triangulo([8, 9, 5])
triangulo_3 = Triangulo([4, 4, 4])

print(str(triangulo_1))
print(str(triangulo_2))
print(str(triangulo_3))



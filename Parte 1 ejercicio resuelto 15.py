class Esferas:
    def __init__(self, peso_a, peso_b, peso_c, peso_d):
        self.peso_a = peso_a
        self.peso_b = peso_b
        self.peso_c = peso_c
        self.peso_d = peso_d

    def determinar_esfera_diferente(self):
        if self.peso_a == self.peso_b and self.peso_a == self.peso_c:
            diferente = "D"
            mayor = self.peso_d > self.peso_a

        elif self.peso_a == self.peso_b and self.peso_a == self.peso_d:
            diferente = "C"
            mayor = self.peso_c > self.peso_a

        elif self.peso_a == self.peso_c and self.peso_a == self.peso_d:
            diferente = "B"
            mayor = self.peso_b > self.peso_a

        else:
            diferente = "A"
            mayor = self.peso_a > self.peso_b
        
        if mayor:
            return f"La esfera {diferente} es la diferente y es de mayor peso."
        else:
            return f"La esfera {diferente} es la diferente y es de menor peso."

peso_a = float(input("Ingrese el peso de la esfera A: "))
peso_b = float(input("Ingrese el peso de la esfera B: "))
peso_c = float(input("Ingrese el peso de la esfera C: "))
peso_d = float(input("Ingrese el peso de la esfera D: "))

esferas = Esferas(peso_a, peso_b, peso_c, peso_d)
resultado = esferas.determinar_esfera_diferente()

print(resultado)
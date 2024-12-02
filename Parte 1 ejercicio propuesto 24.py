class Esfera:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

    def __str__(self):
        return f"Esfera {self.nombre} con peso {self.peso} kg"


class ComparadorEsferas:
    def __init__(self, esfera1, esfera2, esfera3):
        self.esfera1 = esfera1
        self.esfera2 = esfera2
        self.esfera3 = esfera3

    def determinar_mayor_peso(self):
        if self.esfera1.peso > self.esfera2.peso and self.esfera1.peso > self.esfera3.peso:
            return f"La esfera {self.esfera1.nombre} es la de mayor peso."
        elif self.esfera2.peso > self.esfera1.peso and self.esfera2.peso > self.esfera3.peso:
            return f"La esfera {self.esfera2.nombre} es la de mayor peso."
        else:
            return f"La esfera {self.esfera3.nombre} es la de mayor peso."

peso_A = float(input("Ingrese el peso de la esfera A: "))
peso_B = float(input("Ingrese el peso de la esfera B: "))
peso_C = float(input("Ingrese el peso de la esfera C: "))

esfera_A = Esfera("A", peso_A)
esfera_B = Esfera("B", peso_B)
esfera_C = Esfera("C", peso_C)

comparador = ComparadorEsferas(esfera_A, esfera_B, esfera_C)
resultado = comparador.determinar_mayor_peso()

print(resultado)
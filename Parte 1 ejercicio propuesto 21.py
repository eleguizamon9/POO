class Triángulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1= lado1
        self.lado2= lado2
        self.lado3= lado3

    def calcular_perímetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def calcular_área(self):
        s= self.calcular_perímetro()/2
        return (s*(s-self.lado1)*(s-self.lado2)*(self.lado3))**0.5

    def mostrar_info(self):
        print(f"Perímetro: {self.calcular_perímetro():.2f}")
        print(f"Semiperímetro: {self.calcular_perímetro()/2:.2f}")
        print(f"Área: {self.calcular_área():.2f}")

lado1= float(input("Ingrese el lado 1: "))
lado2= float(input("Ingrese el lado 2: "))
lado3= float(input("Ingrese el lado 3: "))

triángulo= Triángulo(lado1, lado2, lado3)

triángulo.mostrar_info()
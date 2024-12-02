class Triángulo_equilátero:
    def __init__(self,lado):
        self.lado=lado

    def calcular_perímetro(self):
        return 3*self.lado
    
    def calcular_altura(self):
        return (((3)**0.5)/2)*self.lado
    
    def calcular_área(self):
        return (((3)**0.5)/4)*(self.lado**2)
    
    def mostrar_info(self):
        print(f"Perímetro: {self.calcular_perímetro():.2f}\nAltura: {self.calcular_altura():.2f}\nÁrea: {self.calcular_área():.2f}")

triángulo=Triángulo_equilátero(float(input("Ingrese el valor del lado del triángulo equilátero: ")))

triángulo.mostrar_info()
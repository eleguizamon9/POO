class EcuaciónSegundoGrado:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_discriminante(self):
        return self.b**2 - 4 * self.a * self.c

    def calcular_soluciones(self):
        discriminante = self.calcular_discriminante()
        if discriminante > 0:
            x1 = (-self.b + (discriminante**(0.5))) / (2 * self.a)
            x2 = (-self.b - (discriminante**(0.5))) / (2 * self.a)
            return f"Dos soluciones reales: x1 = {x1}, x2 = {x2}"
        
        elif discriminante == 0:
            x = -self.b / (2 * self.a)
            return f"Una solución real: x = {x}"
        
        else:
            parte_real = -self.b / (2 * self.a)
            parte_imaginaria = ((-discriminante)**(0.5)) / (2 * self.a)
            return f"Soluciones complejas: x1 = {parte_real} + {parte_imaginaria}i, x2 = {parte_real} - {parte_imaginaria}i"

    def mostrar_resultados(self):
        print("\nResultados de la ecuación:")
        print(self.calcular_soluciones())

a = float(input("Ingrese el valor de A: "))
b = float(input("Ingrese el valor de B: "))
c = float(input("Ingrese el valor de C: "))

ecuacion = EcuaciónSegundoGrado(a, b, c)
ecuacion.mostrar_resultados()
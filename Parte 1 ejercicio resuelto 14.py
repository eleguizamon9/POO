class Empresa:
    def __init__(self, ventas_depto1, ventas_depto2, ventas_depto3, salario_base):
        self.ventas_depto1 = ventas_depto1
        self.ventas_depto2 = ventas_depto2
        self.ventas_depto3 = ventas_depto3
        self.salario_base = salario_base

    def calcular_totales(self):
        self.total_ventas = self.ventas_depto1 + self.ventas_depto2 + self.ventas_depto3
        self.porcentaje_33 = self.total_ventas * 0.33

    def calcular_salario(self, ventas_depto):
        if ventas_depto > self.porcentaje_33:
            return self.salario_base + (self.salario_base * 0.2)
        else:
            return self.salario_base

    def mostrar_salarios(self):
        self.calcular_totales()
        salario_depto1 = self.calcular_salario(self.ventas_depto1)
        salario_depto2 = self.calcular_salario(self.ventas_depto2)
        salario_depto3 = self.calcular_salario(self.ventas_depto3)

        print(f"Salario vendedores Depto. 1: ${salario_depto1:.2f}")
        print(f"Salario vendedores Depto. 2: ${salario_depto2:.2f}")
        print(f"Salario vendedores Depto. 3: ${salario_depto3:.2f}")

ventas_depto1 = float(input("Ingrese las ventas del departamento 1: "))
ventas_depto2 = float(input("Ingrese las ventas del departamento 2: "))
ventas_depto3 = float(input("Ingrese las ventas del departamento 3: "))
salario_base = float(input("Ingrese el salario base de los vendedores: "))

empresa = Empresa(ventas_depto1, ventas_depto2, ventas_depto3, salario_base)
empresa.mostrar_salarios()
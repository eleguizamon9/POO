class Empleado:
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_mensual(self):
        return self.salario_por_hora * self.horas_trabajadas

    def mostrar_informacion(self):
        salario_mensual = self.calcular_salario_mensual()
        if salario_mensual > 450_000:
            return f"Nombre: {self.nombre}\nSalario Mensual: ${salario_mensual:,.2f}"
        else:
            return f"Nombre: {self.nombre}"

nombre = input("Ingrese el nombre del empleado: ")
salario_por_hora = float(input("Ingrese el salario por hora: "))
horas_trabajadas = int(input("Ingrese el número de horas trabajadas en el mes: "))

empleado = Empleado(nombre, salario_por_hora, horas_trabajadas)
resultado = empleado.mostrar_informacion()

print("\nInformación del empleado:")
print(resultado)
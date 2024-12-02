class Trabajador:
    def __init__(self, nombre, horas_trabajadas, valor_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        if self.horas_trabajadas > 40:
            horas_extras = self.horas_trabajadas - 40

            if horas_extras > 8:
                horas_extras_excedentes = horas_extras - 8
                salario = (40 * self.valor_hora + 8 * 2 * self.valor_hora + horas_extras_excedentes * 3 * self.valor_hora)

            else:
                salario = (40 * self.valor_hora + horas_extras * 2 * self.valor_hora)

        else:
            salario = self.horas_trabajadas * self.valor_hora
        
        return salario

    def mostrar_informacion(self):
        salario = self.calcular_salario()
        print(f"EL TRABAJADOR {self.nombre} DEVENGÓ: ${salario:.2f}")

nombre = input("Ingrese el nombre del trabajador: ")
horas_trabajadas = float(input("Ingrese el número de horas trabajadas en la semana: "))
valor_hora = float(input("Ingrese el valor de una hora normal trabajada: "))

trabajador = Trabajador(nombre, horas_trabajadas, valor_hora)

trabajador.mostrar_informacion()
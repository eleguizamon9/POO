class Empleado:
    def __init__(self, código, nombres, horas_trabajadas, valor_hora, porcentaje_retefuente):
        self.código=código
        self.nombres=nombres
        self.horas_trabajadas=horas_trabajadas
        self.valor_hora=valor_hora
        self.porcentaje_retefuente=porcentaje_retefuente

    def calcular_salario_bruto(self):
        return self.horas_trabajadas*self.valor_hora
    
    def calcular_salario_neto(self):
        return self.calcular_salario_bruto()*(1-self.porcentaje_retefuente/100)
    
    def mostrar_info(self):
        print(f"Código: {self.código}\nNombres: {self.nombres}\nSalario Bruto: {self.calcular_salario_bruto()}\nSalario Neto: {self.calcular_salario_neto()}")

código=input("Ingrese el código del empleado: ")
nombres=input("Ingrese el nombre del empleado: ")
horas_trabajadas=int(input("Ingrese las horas trabajadas al mes: "))
valor_hora=float(input("Ingrese el valor por hora trabajada: "))
porcentaje_retefuente=float(input("Ingrese el porcentaje de retención en la fuente: "))

empleado=Empleado(código, nombres, horas_trabajadas, valor_hora, porcentaje_retefuente)

empleado.mostrar_info()
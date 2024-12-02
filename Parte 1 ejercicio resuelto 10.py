class Estudiante:
    def __init__(self, número_inscrpción, nombres, patrimonio, estrato):
        self.número_inscripción= número_inscripción
        self.nombres= nombres
        self.patrimonio= patrimonio
        self.estrato= estrato
        
    def calcular_pago_matrícula(self):
        pago_matrícula= 50000
        
        if self.patrimonio>2000000 and self.estrato>3:
            pago_matrícula+=0.03*self.patrimonio
            
        return pago_matrícula
    
    def mostrar_info(self):
        print(f"Número de inscripción: {self.número_inscripción}")
        print(f"Nombres: {self.nombres}")
        print(f"Pago de matrícula: ${self.calcular_pago_matrícula():.2f}")

número_inscripción= input("Ingrese el número de inscripción del estudiante: ")
nombres= input("Ingrese los nombres del estudiante: ")
patrimonio= float(input("Ingrese el patrimonio del estudiante: "))
estrato= int(input("Ingrese el estrato del estudiante: "))

estudiante= Estudiante(número_inscripción, nombres, patrimonio, estrato)

estudiante.mostrar_info()
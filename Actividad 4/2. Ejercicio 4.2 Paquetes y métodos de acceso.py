class Inmueble:

    def __init__(self):
        self.identificador_inmobiliario = int(input("Ingrese el identificador inmobiliario: "))
        self.area = int(input("Ingrese el área en metros cuadrados: "))
        self.direccion = input("Ingrese la dirección del inmueble: ")
        self.precio_venta = float(input("Ingrese el precio de venta: "))

    def calcular_precio_venta(self):
        valor_area = float(input("Ingrese el valor por metro cuadrado del área: "))
        self.precio_venta = self.area * valor_area
        return self.precio_venta

    def imprimir(self):
        print(f"Identificador inmobiliario = {self.identificador_inmobiliario}")
        print(f"Área = {self.area}")
        print(f"Dirección = {self.direccion}")
        print(f"Precio de venta = ${self.precio_venta:,.2f}")


class InmuebleVivienda(Inmueble):
    
    def __init__(self):
        super().__init__()
        self.numero_habitaciones = int(input("Ingrese el número de habitaciones: "))
        self.numero_banos = int(input("Ingrese el número de baños: "))

    def imprimir(self):
        super().imprimir()
        print(f"Número de habitaciones = {self.numero_habitaciones}")
        print(f"Número de baños = {self.numero_banos}")


class Casa(InmuebleVivienda):
    
    def __init__(self):
        super().__init__()
        self.numero_pisos = int(input("Ingrese el número de pisos: "))

    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos = {self.numero_pisos}")


class Apartamento(InmuebleVivienda):
    
    def __init__(self):
        super().__init__()

    def imprimir(self):
        super().imprimir()


class CasaRural(Casa):
    
    def __init__(self):
        super().__init__()
        self.distancia_cabecera = int(input("Ingrese la distancia a la cabecera municipal (km): "))
        self.altitud = int(input("Ingrese la altitud sobre el nivel del mar (m): "))

    def imprimir(self):
        super().imprimir()
        print(f"Distancia a la cabecera municipal = {self.distancia_cabecera} km")
        print(f"Altitud sobre el nivel del mar = {self.altitud} metros")


class ApartamentoFamiliar(Apartamento):
    
    def __init__(self):
        super().__init__()
        self.valor_administracion = int(input("Ingrese el valor de administración: "))

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = ${self.valor_administracion}")


class Apartaestudio(Apartamento):
    
    def __init__(self):
        super().__init__()

    def imprimir(self):
        super().imprimir()


class Local(Inmueble):
    
    def __init__(self):
        super().__init__()
        self.tipo_local = input("Ingrese el tipo de local (Interno/Calle): ")

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local = {self.tipo_local}")


class LocalComercial(Local):
    
    def __init__(self):
        super().__init__()
        self.centro_comercial = input("Ingrese el nombre del centro comercial: ")

    def imprimir(self):
        super().imprimir()
        print(f"Centro comercial = {self.centro_comercial}")


class Oficina(Local):
    
    def __init__(self):
        super().__init__()
        self.es_gobierno = input("¿Es una oficina gubernamental? (Sí/No): ").strip().lower() == "sí"

    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental = {self.es_gobierno}")


def main():
    print("Creando un Apartamento Familiar...")
    apto1 = ApartamentoFamiliar()
    apto1.calcular_precio_venta()
    apto1.imprimir()

    print("\nCreando un Apartaestudio...")
    aptestudio1 = Apartaestudio()
    aptestudio1.calcular_precio_venta()
    aptestudio1.imprimir()


if __name__ == "__main__":
    main()
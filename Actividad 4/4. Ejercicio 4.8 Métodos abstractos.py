from abc import ABC, abstractmethod

class Ciclista(ABC):
    def __init__(self, identificador, nombre):
        self._identificador = identificador
        self._nombre = nombre
        self._tiempo_acumulado = 0
    
    @abstractmethod
    def imprimir_tipo(self):
        pass
    
    def get_identificador(self):
        return self._identificador
    
    def set_identificador(self, identificador):
        self._identificador = identificador
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_tiempo_acumulado(self):
        return self._tiempo_acumulado
    
    def set_tiempo_acumulado(self, tiempo):
        self._tiempo_acumulado = tiempo
    
    def imprimir(self):
        print(f"Identificador = {self._identificador}")
        print(f"Nombre = {self._nombre}")
        print(f"Tiempo Acumulado = {self._tiempo_acumulado}")


class Velocista(Ciclista):
    def __init__(self, identificador, nombre, potencia_promedio, velocidad_promedio):
        super().__init__(identificador, nombre)
        self._potencia_promedio = potencia_promedio
        self._velocidad_promedio = velocidad_promedio
    
    def imprimir_tipo(self):
        return "Es un velocista"
    
    def imprimir(self):
        super().imprimir()
        print(f"Potencia promedio = {self._potencia_promedio}")
        print(f"Velocidad promedio = {self._velocidad_promedio}")


class Escalador(Ciclista):
    def __init__(self, identificador, nombre, aceleracion_promedio, grado_rampa):
        super().__init__(identificador, nombre)
        self._aceleracion_promedio = aceleracion_promedio
        self._grado_rampa = grado_rampa
    
    def imprimir_tipo(self):
        return "Es un escalador"
    
    def imprimir(self):
        super().imprimir()
        print(f"Aceleración promedio = {self._aceleracion_promedio}")
        print(f"Grado de rampa = {self._grado_rampa}")


class Contrarrelojista(Ciclista):
    def __init__(self, identificador, nombre, velocidad_maxima):
        super().__init__(identificador, nombre)
        self._velocidad_maxima = velocidad_maxima
    
    def imprimir_tipo(self):
        return "Es un contrarrelojista"
    
    def imprimir(self):
        super().imprimir()
        print(f"Velocidad máxima = {self._velocidad_maxima}")


class Equipo:
    def __init__(self, nombre, pais):
        self._nombre = nombre
        self._pais = pais
        self._total_tiempo = 0
        self._lista_ciclistas = []
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_pais(self):
        return self._pais
    
    def set_pais(self, pais):
        self._pais = pais
    
    def añadir_ciclista(self, ciclista):
        self._lista_ciclistas.append(ciclista)
    
    def listar_equipo(self):
        for ciclista in self._lista_ciclistas:
            print(ciclista.get_nombre())
    
    def buscar_ciclista(self, nombre_ciclista):
        for ciclista in self._lista_ciclistas:
            if ciclista.get_nombre() == nombre_ciclista:
                ciclista.imprimir()
                return
        print("Ciclista no encontrado")
    
    def calcular_total_tiempo(self):
        self._total_tiempo = sum(c.get_tiempo_acumulado() for c in self._lista_ciclistas)
    
    def imprimir(self):
        print(f"Nombre del equipo = {self._nombre}")
        print(f"País = {self._pais}")
        print(f"Total tiempo del equipo = {self._total_tiempo}")


# Prueba del programa
def main():
    nombre_equipo = input("Ingrese el nombre del equipo: ")
    pais_equipo = input("Ingrese el país del equipo: ")
    equipo1 = Equipo(nombre_equipo, pais_equipo)
    
    print("\nCreando velocista...")
    identificador = int(input("Ingrese el identificador del velocista: "))
    nombre = input("Ingrese el nombre del velocista: ")
    potencia_promedio = float(input("Ingrese la potencia promedio del velocista: "))
    velocidad_promedio = float(input("Ingrese la velocidad promedio del velocista: "))
    velocista1 = Velocista(identificador, nombre, potencia_promedio, velocidad_promedio)
    
    print("\nCreando escalador...")
    identificador = int(input("Ingrese el identificador del escalador: "))
    nombre = input("Ingrese el nombre del escalador: ")
    aceleracion_promedio = float(input("Ingrese la aceleración promedio del escalador: "))
    grado_rampa = float(input("Ingrese el grado de rampa soportado por el escalador: "))
    escalador1 = Escalador(identificador, nombre, aceleracion_promedio, grado_rampa)
    
    print("\nCreando contrarrelojista...")
    identificador = int(input("Ingrese el identificador del contrarrelojista: "))
    nombre = input("Ingrese el nombre del contrarrelojista: ")
    velocidad_maxima = float(input("Ingrese la velocidad máxima del contrarrelojista: "))
    contrarrelojista1 = Contrarrelojista(identificador, nombre, velocidad_maxima)
    
    equipo1.añadir_ciclista(velocista1)
    equipo1.añadir_ciclista(escalador1)
    equipo1.añadir_ciclista(contrarrelojista1)
    
    velocista1.set_tiempo_acumulado(int(input("Ingrese el tiempo acumulado del velocista: ")))
    escalador1.set_tiempo_acumulado(int(input("Ingrese el tiempo acumulado del escalador: ")))
    contrarrelojista1.set_tiempo_acumulado(int(input("Ingrese el tiempo acumulado del contrarrelojista: ")))
    
    equipo1.calcular_total_tiempo()
    equipo1.imprimir()
    equipo1.listar_equipo()

if __name__ == "__main__":
    main()
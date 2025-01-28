class Cuenta:
    """
    Clase que modela una cuenta bancaria con los atributos saldo, número de consignaciones,
    número de retiros, tasa anual de interés y comisión mensual.
    """
    def __init__(self, saldo: float, tasa_anual: float):
        self.saldo = saldo
        self.numero_consignaciones = 0
        self.numero_retiros = 0
        self.tasa_anual = tasa_anual
        self.comision_mensual = 0

    def consignar(self, cantidad: float):
        """
        Método que recibe una cantidad de dinero a consignar y actualiza el saldo de la cuenta.
        """
        self.saldo += cantidad
        self.numero_consignaciones += 1

    def retirar(self, cantidad: float):
        """
        Método que recibe una cantidad de dinero a retirar y actualiza el saldo de la cuenta.
        """
        nuevo_saldo = self.saldo - cantidad
        if nuevo_saldo >= 0:
            self.saldo -= cantidad
            self.numero_retiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual.")

    def calcular_interes(self):
        """
        Método que calcula el interés mensual de la cuenta a partir de la tasa anual aplicada.
        """
        tasa_mensual = self.tasa_anual / 12
        interes_mensual = self.saldo * tasa_mensual
        self.saldo += interes_mensual

    def extracto_mensual(self):
        """
        Método que genera un extracto aplicando la comisión mensual y calculando los intereses.
        """
        self.saldo -= self.comision_mensual
        self.calcular_interes()

    def imprimir(self):
        """
        Método que muestra el saldo, la comisión mensual y el número de transacciones.
        """
        print(f"Saldo: ${self.saldo:.2f}")
        print(f"Comisión mensual: ${self.comision_mensual:.2f}")
        print(f"Número de transacciones: {self.numero_consignaciones + self.numero_retiros}")


class CuentaAhorros(Cuenta):
    """
    Clase que modela una cuenta de ahorros, subclase de Cuenta.
    """
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)
        self.activa = saldo >= 10000

    def retirar(self, cantidad: float):
        """
        Método para retirar dinero de la cuenta de ahorros.
        """
        if self.activa:
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        """
        Método para consignar dinero en la cuenta de ahorros.
        """
        if self.activa:
            super().consignar(cantidad)

    def extracto_mensual(self):
        """
        Método que genera el extracto mensual de la cuenta de ahorros.
        """
        if self.numero_retiros > 4:
            self.comision_mensual += (self.numero_retiros - 4) * 1000
        super().extracto_mensual()
        self.activa = self.saldo >= 10000

    def imprimir(self):
        """
        Método que muestra los datos de una cuenta de ahorros.
        """
        super().imprimir()
        print()


class CuentaCorriente(Cuenta):
    """
    Clase que modela una cuenta corriente, subclase de Cuenta.
    """
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)
        self.sobregiro = 0

    def retirar(self, cantidad: float):
        """
        Método para retirar dinero de la cuenta corriente. Puede generar sobregiro.
        """
        resultado = self.saldo - cantidad
        if resultado < 0:
            self.sobregiro -= resultado
            self.saldo = 0
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        """
        Método para consignar dinero en la cuenta corriente. Reduce el sobregiro si existe.
        """
        if self.sobregiro > 0:
            residuo = self.sobregiro - cantidad
            if residuo > 0:
                self.sobregiro = 0
                self.saldo = residuo
            else:
                self.sobregiro = -residuo
                self.saldo = 0
        else:
            super().consignar(cantidad)

    def extracto_mensual(self):
        """
        Método que genera el extracto mensual de la cuenta corriente.
        """
        super().extracto_mensual()

    def imprimir(self):
        """
        Método que muestra los datos de una cuenta corriente.
        """
        super().imprimir()
        print(f"Valor de sobregiro: ${self.sobregiro:.2f}")
        print()


# Método main
def main():
    print("Cuenta de ahorros")
    saldo_inicial = float(input("Ingrese saldo inicial: $"))
    tasa_anual = float(input("Ingrese tasa de interés: "))
    
    cuenta_ahorros = CuentaAhorros(saldo_inicial, tasa_anual)
    
    cantidad_consignar = float(input("Ingresar cantidad a consignar: $"))
    cuenta_ahorros.consignar(cantidad_consignar)
    
    cantidad_retirar = float(input("Ingresar cantidad a retirar: $"))
    cuenta_ahorros.retirar(cantidad_retirar)
    
    cuenta_ahorros.extracto_mensual()
    cuenta_ahorros.imprimir()

if __name__ == "__main__":
    main()
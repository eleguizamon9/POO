class Promoción_almacén:
    def __init__(self, valor_compra, color_bolita):
        self.valor_compra = valor_compra
        self.color_bolita = color_bolita.lower()

    def calcular_descuento(self):
        if self.color_bolita == "blanco":
            porcentaje_descuento = 0
        elif self.color_bolita == "verde":
            porcentaje_descuento = 10
        elif self.color_bolita == "amarillo":
            porcentaje_descuento = 25
        elif self.color_bolita == "azul":
            porcentaje_descuento = 50
        else:
            porcentaje_descuento = 100

        valor_pagar = self.valor_compra - (porcentaje_descuento * self.valor_compra / 100)
        return valor_pagar

    def mostrar_resultado(self):
        valor_final = self.calcular_descuento()
        print(f"El cliente debe pagar: ${valor_final:.2f}")

valor_compra = float(input("Ingrese el valor de la compra: "))
color_bolita = input("Ingrese el color de la bolita que sacó: ")

promocion = Promoción_almacén(valor_compra, color_bolita)

promocion.mostrar_resultado()
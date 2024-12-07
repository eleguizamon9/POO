import math

class Circulo:
    """
    Esta clase define objetos de tipo Círculo con su radio como atributo.
    """
    def __init__(self, radio):
        """
        Constructor de la clase Círculo
        :param radio: Parámetro que define el radio de un círculo
        """
        self.radio = radio

    def calcular_area(self):
        """
        Método que calcula y devuelve el área de un círculo como pi multiplicado por el radio al cuadrado
        :return: Área de un círculo
        """
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        """
        Método que calcula y devuelve el perímetro de un círculo como la multiplicación de pi por el radio por 2
        :return: Perímetro de un círculo
        """
        return 2 * math.pi * self.radio


class Rectangulo:
    """
    Esta clase define objetos de tipo Rectángulo con una base y una altura como atributos.
    """
    def __init__(self, base, altura):
        """
        Constructor de la clase Rectangulo
        :param base: Parámetro que define la base de un rectángulo
        :param altura: Parámetro que define la altura de un rectángulo
        """
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """
        Método que calcula y devuelve el área de un rectángulo como la multiplicación de la base por la altura
        :return: Área de un rectángulo
        """
        return self.base * self.altura

    def calcular_perimetro(self):
        """
        Método que calcula y devuelve el perímetro de un rectángulo como (2 * base) + (2 * altura)
        :return: Perímetro de un rectángulo
        """
        return (2 * self.base) + (2 * self.altura)


class Cuadrado:
    """
    Esta clase define objetos de tipo Cuadrado con un lado como atributo.
    """
    def __init__(self, lado):
        """
        Constructor de la clase Cuadrado
        :param lado: Parámetro que define la longitud de la base de un cuadrado
        """
        self.lado = lado

    def calcular_area(self):
        """
        Método que calcula y devuelve el área de un cuadrado como el lado elevado al cuadrado
        :return: Área de un Cuadrado
        """
        return self.lado ** 2

    def calcular_perimetro(self):
        """
        Método que calcula y devuelve el perímetro de un cuadrado como cuatro veces su lado
        :return: Perímetro de un cuadrado
        """
        return 4 * self.lado


class TrianguloRectangulo:
    """
    Esta clase define objetos de tipo Triángulo Rectángulo con una base y una altura como atributos.
    """
    def __init__(self, base, altura):
        """
        Constructor de la clase TriánguloRectángulo
        :param base: Parámetro que define la base de un triángulo rectángulo
        :param altura: Parámetro que define la altura de un triángulo rectángulo
        """
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """
        Método que calcula y devuelve el área de un triángulo rectángulo
        como la base multiplicada por la altura sobre 2
        :return: Área de un triángulo rectángulo
        """
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self):
        """
        Método que calcula y devuelve la hipotenusa de un triángulo rectángulo
        utilizando el teorema de Pitágoras
        :return: Hipotenusa de un triángulo rectángulo
        """
        return math.sqrt((self.base ** 2) + (self.altura ** 2))

    def calcular_perimetro(self):
        """
        Método que calcula y devuelve el perímetro de un triángulo rectángulo
        como la suma de la base, la altura y la hipotenusa
        :return: Perímetro de un triángulo rectángulo
        """
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self):
        """
        Método que determina si un triángulo es:
        - Equilatero: si sus tres lados son iguales
        - Escaleno: si sus tres lados son todos diferentes
        - Isósceles: si dos de sus lados son iguales
        """
        hip = self.calcular_hipotenusa()
        
        # Para comparar considerando posible inexactitud en float, se usa round
        base_rounded = round(self.base, 5)
        altura_rounded = round(self.altura, 5)
        hip_rounded = round(hip, 5)

        if base_rounded == altura_rounded == hip_rounded:
            print("Es un triángulo equilátero")
        elif (base_rounded != altura_rounded) and (base_rounded != hip_rounded) and (altura_rounded != hip_rounded):
            print("Es un triángulo escaleno")
        else:
            print("Es un triángulo isósceles")


# Clase de prueba
if __name__ == "__main__":
    figura1 = Circulo(2)
    figura2 = Rectangulo(1, 2)
    figura3 = Cuadrado(3)
    figura4 = TrianguloRectangulo(3, 5)

    print("El área del círculo es =", figura1.calcular_area())
    print("El perímetro del círculo es =", figura1.calcular_perimetro())
    print()

    print("El área del rectángulo es =", figura2.calcular_area())
    print("El perímetro del rectángulo es =", figura2.calcular_perimetro())
    print()

    print("El área del cuadrado es =", figura3.calcular_area())
    print("El perímetro del cuadrado es =", figura3.calcular_perimetro())
    print()

    print("El área del triángulo es =", figura4.calcular_area())
    print("El perímetro del triángulo es =", figura4.calcular_perimetro())
    figura4.determinar_tipo_triangulo()
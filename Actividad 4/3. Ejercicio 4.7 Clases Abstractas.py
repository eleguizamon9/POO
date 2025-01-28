from abc import ABC, abstractmethod

# Clase base abstracta
class Animal(ABC):
    """
    Clase abstracta que modela un animal con los atributos sonido, alimentos, hábitat y nombre científico.
    """
    def __init__(self):
        self.nombre_cientifico = input("Ingrese el nombre científico del animal: ")
        self.sonido = input("Ingrese el sonido característico del animal: ")
        self.alimentos = input("Ingrese el tipo de alimentación del animal: ")
        self.habitat = input("Ingrese el hábitat del animal: ")

    @abstractmethod
    def get_nombre_cientifico(self):
        pass

    @abstractmethod
    def get_sonido(self):
        pass

    @abstractmethod
    def get_alimentos(self):
        pass

    @abstractmethod
    def get_habitat(self):
        pass


# Subclases abstractas
class Canido(Animal):
    """
    Clase abstracta para los cánidos.
    """
    pass


class Felino(Animal):
    """
    Clase abstracta para los felinos.
    """
    pass


# Subclases concretas
class Perro(Canido):
    def __init__(self):
        super().__init__()

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


class Lobo(Canido):
    def __init__(self):
        super().__init__()

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


class Leon(Felino):
    def __init__(self):
        super().__init__()

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


class Gato(Felino):
    def __init__(self):
        super().__init__()

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


# Método de prueba
def main():
    """
    Función principal que crea un array de varios animales y muestra su información.
    """
    print("Creando un Gato...")
    gato = Gato()
    print("\nCreando un Perro...")
    perro = Perro()
    print("\nCreando un Lobo...")
    lobo = Lobo()
    print("\nCreando un León...")
    leon = Leon()

    animales = [gato, perro, lobo, leon]

    for animal in animales:
        print("\nInformación del animal:")
        print(f"Nombre científico: {animal.get_nombre_cientifico()}")
        print(f"Sonido: {animal.get_sonido()}")
        print(f"Alimentos: {animal.get_alimentos()}")
        print(f"Hábitat: {animal.get_habitat()}\n")


if __name__ == "__main__":
    main()
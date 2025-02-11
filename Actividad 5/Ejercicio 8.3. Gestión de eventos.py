import math
import tkinter as tk
from tkinter import messagebox


class FiguraGeometrica:
    """
    Clase base para figuras geométricas, con volumen y superficie.
    """
    def __init__(self):
        self.volumen = 0
        self.superficie = 0

    def set_volumen(self, volumen):
        self.volumen = volumen

    def set_superficie(self, superficie):
        self.superficie = superficie

    def get_volumen(self):
        return self.volumen

    def get_superficie(self):
        return self.superficie


class Cilindro(FiguraGeometrica):
    """
    Clase que modela un cilindro con radio y altura.
    """
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return math.pi * self.altura * self.radio ** 2

    def calcular_superficie(self):
        area_lateral = 2 * math.pi * self.radio * self.altura
        area_base = 2 * math.pi * self.radio ** 2
        return area_lateral + area_base


class Esfera(FiguraGeometrica):
    """
    Clase que modela una esfera con un radio dado.
    """
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return (4/3) * math.pi * self.radio ** 3

    def calcular_superficie(self):
        return 4 * math.pi * self.radio ** 2


class Piramide(FiguraGeometrica):
    """
    Clase que modela una pirámide con base, altura y apotema.
    """
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return (self.base ** 2 * self.altura) / 3

    def calcular_superficie(self):
        area_base = self.base ** 2
        area_lados = 2 * self.base * self.apotema
        return area_base + area_lados


class VentanaCilindro:
    """
    Ventana para calcular el volumen y la superficie de un cilindro.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Cilindro")
        self.root.geometry("280x210")
        self.root.resizable(False, False)

        tk.Label(root, text="Radio (cms):").place(x=20, y=20)
        self.campo_radio = tk.Entry(root)
        self.campo_radio.place(x=100, y=20)

        tk.Label(root, text="Altura (cms):").place(x=20, y=50)
        self.campo_altura = tk.Entry(root)
        self.campo_altura.place(x=100, y=50)

        self.boton_calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.boton_calcular.place(x=100, y=80)

        self.volumen = tk.Label(root, text="Volumen (cm³): ")
        self.volumen.place(x=20, y=110)

        self.superficie = tk.Label(root, text="Superficie (cm²): ")
        self.superficie.place(x=20, y=140)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            altura = float(self.campo_altura.get())
            cilindro = Cilindro(radio, altura)

            self.volumen.config(text=f"Volumen (cm³): {cilindro.get_volumen():.2f}")
            self.superficie.config(text=f"Superficie (cm²): {cilindro.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese solo valores numéricos")


class VentanaEsfera:
    """
    Ventana para calcular el volumen y la superficie de una esfera.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Esfera")
        self.root.geometry("280x200")
        self.root.resizable(False, False)

        tk.Label(root, text="Radio (cms):").place(x=20, y=20)
        self.campo_radio = tk.Entry(root)
        self.campo_radio.place(x=100, y=20)

        self.boton_calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.boton_calcular.place(x=100, y=50)

        self.volumen = tk.Label(root, text="Volumen (cm³): ")
        self.volumen.place(x=20, y=90)

        self.superficie = tk.Label(root, text="Superficie (cm²): ")
        self.superficie.place(x=20, y=120)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            esfera = Esfera(radio)

            self.volumen.config(text=f"Volumen (cm³): {esfera.get_volumen():.2f}")
            self.superficie.config(text=f"Superficie (cm²): {esfera.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese solo valores numéricos")


class VentanaPiramide:
    """
    Ventana para calcular el volumen y la superficie de una pirámide.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Pirámide")
        self.root.geometry("280x240")
        self.root.resizable(False, False)

        tk.Label(root, text="Base (cms):").place(x=20, y=20)
        self.campo_base = tk.Entry(root)
        self.campo_base.place(x=120, y=20)

        tk.Label(root, text="Altura (cms):").place(x=20, y=50)
        self.campo_altura = tk.Entry(root)
        self.campo_altura.place(x=120, y=50)

        tk.Label(root, text="Apotema (cms):").place(x=20, y=80)
        self.campo_apotema = tk.Entry(root)
        self.campo_apotema.place(x=120, y=80)

        self.boton_calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.boton_calcular.place(x=120, y=110)

        self.volumen = tk.Label(root, text="Volumen (cm³): ")
        self.volumen.place(x=20, y=140)

        self.superficie = tk.Label(root, text="Superficie (cm²): ")
        self.superficie.place(x=20, y=170)

    def calcular(self):
        try:
            base = float(self.campo_base.get())
            altura = float(self.campo_altura.get())
            apotema = float(self.campo_apotema.get())

            piramide = Piramide(base, altura, apotema)

            self.volumen.config(text=f"Volumen (cm³): {piramide.get_volumen():.2f}")
            self.superficie.config(text=f"Superficie (cm²): {piramide.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese solo valores numéricos")


class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Figuras")
        self.root.geometry("350x160")

        tk.Button(root, text="Cilindro", command=self.abrir_cilindro).place(x=20, y=50)
        tk.Button(root, text="Esfera", command=self.abrir_esfera).place(x=125, y=50)
        tk.Button(root, text="Pirámide", command=self.abrir_piramide).place(x=225, y=50)

    def abrir_cilindro(self):
        VentanaCilindro(tk.Toplevel(self.root))

    def abrir_esfera(self):
        VentanaEsfera(tk.Toplevel(self.root))

    def abrir_piramide(self):
        VentanaPiramide(tk.Toplevel(self.root))


if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
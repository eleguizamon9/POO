import tkinter as tk
from tkinter import messagebox
import math

# Clases geométricas

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self):
        return math.sqrt((self.base ** 2) + (self.altura ** 2))

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self):
        hip = self.calcular_hipotenusa()
        lados = sorted([self.base, self.altura, hip])
        if lados[0] == lados[1] == lados[2]:
            return "Equilátero"
        elif lados[0] != lados[1] and lados[1] != lados[2]:
            return "Escaleno"
        else:
            return "Isósceles"


# Clase de la interfaz gráfica

class InterfazFiguras:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Figuras Geométricas")
        self.ventana.geometry("400x250")
        self.ventana.configure(bg="#f0f8ff")

        # Título
        titulo = tk.Label(ventana, text="Cálculos de Figuras Geométricas", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
        titulo.pack(pady=10)

        # Botones para seleccionar la figura
        tk.Button(ventana, text="Círculo", font=("Arial", 12), bg="#4caf50", fg="white", command=self.interfaz_circulo).pack(pady=5)
        tk.Button(ventana, text="Rectángulo", font=("Arial", 12), bg="#2196f3", fg="white", command=self.interfaz_rectangulo).pack(pady=5)
        tk.Button(ventana, text="Cuadrado", font=("Arial", 12), bg="#ff9800", fg="white", command=self.interfaz_cuadrado).pack(pady=5)
        tk.Button(ventana, text="Triángulo Rectángulo", font=("Arial", 12), bg="#9c27b0", fg="white", command=self.interfaz_triangulo).pack(pady=5)

    def mostrar_resultado(self, mensaje):
        """
        Muestra el resultado en un cuadro de diálogo.
        """
        messagebox.showinfo("Resultado", mensaje)

    def interfaz_circulo(self):
        """
        Interfaz para calcular el área y el perímetro de un círculo.
        """
        def calcular():
            try:
                radio = float(entry_radio.get())
                circulo = Circulo(radio)
                area = circulo.calcular_area()
                perimetro = circulo.calcular_perimetro()
                self.mostrar_resultado(f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un valor válido para el radio.")

        ventana_circulo = tk.Toplevel(self.ventana)
        ventana_circulo.title("Círculo")
        ventana_circulo.geometry("300x200")
        tk.Label(ventana_circulo, text="Radio:", font=("Arial", 12)).pack(pady=5)
        entry_radio = tk.Entry(ventana_circulo, font=("Arial", 12))
        entry_radio.pack(pady=5)
        tk.Button(ventana_circulo, text="Calcular", font=("Arial", 12), bg="#4caf50", fg="white", command=calcular).pack(pady=10)

    def interfaz_rectangulo(self):
        """
        Interfaz para calcular el área y el perímetro de un rectángulo.
        """
        def calcular():
            try:
                base = float(entry_base.get())
                altura = float(entry_altura.get())
                rectangulo = Rectangulo(base, altura)
                area = rectangulo.calcular_area()
                perimetro = rectangulo.calcular_perimetro()
                self.mostrar_resultado(f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

        ventana_rectangulo = tk.Toplevel(self.ventana)
        ventana_rectangulo.title("Rectángulo")
        ventana_rectangulo.geometry("300x200")
        tk.Label(ventana_rectangulo, text="Base:", font=("Arial", 12)).pack(pady=5)
        entry_base = tk.Entry(ventana_rectangulo, font=("Arial", 12))
        entry_base.pack(pady=5)
        tk.Label(ventana_rectangulo, text="Altura:", font=("Arial", 12)).pack(pady=5)
        entry_altura = tk.Entry(ventana_rectangulo, font=("Arial", 12))
        entry_altura.pack(pady=5)
        tk.Button(ventana_rectangulo, text="Calcular", font=("Arial", 12), bg="#4caf50", fg="white", command=calcular).pack(pady=10)

    def interfaz_cuadrado(self):
        """
        Interfaz para calcular el área y el perímetro de un cuadrado.
        """
        def calcular():
            try:
                lado = float(entry_lado.get())
                cuadrado = Cuadrado(lado)
                area = cuadrado.calcular_area()
                perimetro = cuadrado.calcular_perimetro()
                self.mostrar_resultado(f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un valor válido.")

        ventana_cuadrado = tk.Toplevel(self.ventana)
        ventana_cuadrado.title("Cuadrado")
        ventana_cuadrado.geometry("300x200")
        tk.Label(ventana_cuadrado, text="Lado:", font=("Arial", 12)).pack(pady=5)
        entry_lado = tk.Entry(ventana_cuadrado, font=("Arial", 12))
        entry_lado.pack(pady=5)
        tk.Button(ventana_cuadrado, text="Calcular", font=("Arial", 12), bg="#4caf50", fg="white", command=calcular).pack(pady=10)

    def interfaz_triangulo(self):
        """
        Interfaz para calcular el área, perímetro y tipo de un triángulo rectángulo.
        """
        def calcular():
            try:
                base = float(entry_base.get())
                altura = float(entry_altura.get())
                triangulo = TrianguloRectangulo(base, altura)
                area = triangulo.calcular_area()
                perimetro = triangulo.calcular_perimetro()
                tipo = triangulo.determinar_tipo_triangulo()
                self.mostrar_resultado(f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}\nTipo: {tipo}")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

        ventana_triangulo = tk.Toplevel(self.ventana)
        ventana_triangulo.title("Triángulo Rectángulo")
        ventana_triangulo.geometry("300x300")
        tk.Label(ventana_triangulo, text="Base:", font=("Arial", 12)).pack(pady=5)
        entry_base = tk.Entry(ventana_triangulo, font=("Arial", 12))
        entry_base.pack(pady=5)
        tk.Label(ventana_triangulo, text="Altura:", font=("Arial", 12)).pack(pady=5)
        entry_altura = tk.Entry(ventana_triangulo, font=("Arial", 12))
        entry_altura.pack(pady=5)
        tk.Button(ventana_triangulo, text="Calcular", font=("Arial", 12), bg="#4caf50", fg="white", command=calcular).pack(pady=10)


# Main
if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazFiguras(ventana)
    ventana.mainloop()
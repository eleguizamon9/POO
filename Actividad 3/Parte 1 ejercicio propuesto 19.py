import tkinter as tk
from tkinter import messagebox

class TrianguloEquilatero:
    def __init__(self, lado):
        self.lado = lado

    def calcular_perimetro(self):
        return 3 * self.lado

    def calcular_altura(self):
        return (3**0.5 / 2) * self.lado

    def calcular_area(self):
        return (3**0.5 / 4) * (self.lado ** 2)


class InterfazTriangulo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Triángulo Equilátero")
        self.ventana.geometry("400x270")
        self.ventana.configure(bg="#f0f8ff")

        titulo = tk.Label(ventana, text="Cálculos de Triángulo Equilátero", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
        titulo.pack(pady=10)

        tk.Label(ventana, text="Ingrese el valor del lado:", font=("Arial", 12), bg="#f0f8ff", fg="#333").pack(pady=5)
        self.entrada_lado = tk.Entry(ventana, font=("Arial", 12))
        self.entrada_lado.pack(pady=5)

        boton = tk.Button(ventana, text="Calcular", font=("Arial", 12), bg="#4caf50", fg="white", command=self.calcular_resultados)
        boton.pack(pady=10)

        self.resultados = tk.Label(ventana, text="", font=("Arial", 12), bg="#f0f8ff", fg="#333", justify="left")
        self.resultados.pack(pady=10)

    def calcular_resultados(self):
        try:
            lado = float(self.entrada_lado.get())

            triangulo = TrianguloEquilatero(lado)

            perimetro = triangulo.calcular_perimetro()
            altura = triangulo.calcular_altura()
            area = triangulo.calcular_area()

            mensaje = (f"Perímetro: {perimetro:.2f} unidades\n"
                       f"Altura: {altura:.2f} unidades\n"
                       f"Área: {area:.2f} unidades cuadradas")
            self.resultados.config(text=mensaje)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")


ventana_principal = tk.Tk()
app = InterfazTriangulo(ventana_principal)
ventana_principal.mainloop()
import math
import tkinter as tk
from tkinter import messagebox

class Notas:
    def __init__(self):
        self.lista_notas = [0] * 5  # Lista para almacenar las 5 notas

    def calcular_promedio(self):
        return sum(self.lista_notas) / len(self.lista_notas)

    def calcular_desviacion(self):
        promedio = self.calcular_promedio()
        suma = sum((nota - promedio) ** 2 for nota in self.lista_notas)
        return math.sqrt(suma / len(self.lista_notas))

    def calcular_menor(self):
        return min(self.lista_notas)

    def calcular_mayor(self):
        return max(self.lista_notas)


class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Notas")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.notas = Notas()

        # Etiquetas y Campos de Texto
        tk.Label(root, text="Nota 1:").place(x=20, y=20)
        self.campo_nota1 = tk.Entry(root)
        self.campo_nota1.place(x=100, y=20, width=150)

        tk.Label(root, text="Nota 2:").place(x=20, y=50)
        self.campo_nota2 = tk.Entry(root)
        self.campo_nota2.place(x=100, y=50, width=150)

        tk.Label(root, text="Nota 3:").place(x=20, y=80)
        self.campo_nota3 = tk.Entry(root)
        self.campo_nota3.place(x=100, y=80, width=150)

        tk.Label(root, text="Nota 4:").place(x=20, y=110)
        self.campo_nota4 = tk.Entry(root)
        self.campo_nota4.place(x=100, y=110, width=150)

        tk.Label(root, text="Nota 5:").place(x=20, y=140)
        self.campo_nota5 = tk.Entry(root)
        self.campo_nota5.place(x=100, y=140, width=150)

        # Botones
        tk.Button(root, text="Calcular", command=self.calcular).place(x=20, y=170, width=100)
        tk.Button(root, text="Limpiar", command=self.limpiar).place(x=140, y=170, width=100)

        # Etiquetas de resultados
        self.promedio = tk.Label(root, text="Promedio = ")
        self.promedio.place(x=20, y=210)

        self.desviacion = tk.Label(root, text="Desviación estándar = ")
        self.desviacion.place(x=20, y=240)

        self.mayor = tk.Label(root, text="Nota mayor = ")
        self.mayor.place(x=20, y=270)

        self.menor = tk.Label(root, text="Nota menor = ")
        self.menor.place(x=20, y=300)

    def calcular(self):
        try:
            # Obtener y convertir las notas a float
            self.notas.lista_notas[0] = float(self.campo_nota1.get())
            self.notas.lista_notas[1] = float(self.campo_nota2.get())
            self.notas.lista_notas[2] = float(self.campo_nota3.get())
            self.notas.lista_notas[3] = float(self.campo_nota4.get())
            self.notas.lista_notas[4] = float(self.campo_nota5.get())

            # Calcular resultados
            promedio = self.notas.calcular_promedio()
            desviacion = self.notas.calcular_desviacion()
            mayor = self.notas.calcular_mayor()
            menor = self.notas.calcular_menor()

            # Mostrar resultados
            self.promedio.config(text=f"Promedio = {promedio:.2f}")
            self.desviacion.config(text=f"Desviación estándar = {desviacion:.2f}")
            self.mayor.config(text=f"Nota mayor = {mayor}")
            self.menor.config(text=f"Nota menor = {menor}")

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese solo valores numéricos")

    def limpiar(self):
        self.campo_nota1.delete(0, tk.END)
        self.campo_nota2.delete(0, tk.END)
        self.campo_nota3.delete(0, tk.END)
        self.campo_nota4.delete(0, tk.END)
        self.campo_nota5.delete(0, tk.END)

        self.promedio.config(text="Promedio = ")
        self.desviacion.config(text="Desviación estándar = ")
        self.mayor.config(text="Nota mayor = ")
        self.menor.config(text="Nota menor = ")


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
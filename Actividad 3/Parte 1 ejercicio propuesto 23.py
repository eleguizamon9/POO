import tkinter as tk
from tkinter import messagebox

class EcuacionSegundoGrado:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_discriminante(self):
        return self.b**2 - 4 * self.a * self.c

    def calcular_soluciones(self):
        discriminante = self.calcular_discriminante()

        if discriminante > 0:
            x1 = (-self.b + discriminante**0.5) / (2 * self.a)
            x2 = (-self.b - discriminante**0.5) / (2 * self.a)
            return f"Dos soluciones reales: x1 = {x1:.2f}, x2 = {x2:.2f}"
        elif discriminante == 0:
            x = -self.b / (2 * self.a)
            return f"Una solución real: x = {x:.2f}"
        else:
            parte_real = -self.b / (2 * self.a)
            parte_imaginaria = (-discriminante)**0.5 / (2 * self.a)
            return (f"Soluciones complejas: x1 = {parte_real:.2f} + {parte_imaginaria:.2f}i, "
                    f"x2 = {parte_real:.2f} - {parte_imaginaria:.2f}i")


class InterfazEcuacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Resolución de Ecuación de Segundo Grado")
        self.ventana.geometry("500x400")
        self.ventana.configure(bg="#f0f8ff")

        titulo = tk.Label(ventana, text="Ecuación de Segundo Grado", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
        titulo.pack(pady=10)

        self.crear_campo("Coeficiente A:", "a")
        self.crear_campo("Coeficiente B:", "b")
        self.crear_campo("Coeficiente C:", "c")

        boton = tk.Button(ventana, text="Calcular Soluciones", font=("Arial", 12), bg="#4caf50", fg="white",
                          command=self.calcular_soluciones)
        boton.pack(pady=10)

        self.resultados = tk.Label(ventana, text="", font=("Arial", 12), bg="#f0f8ff", fg="#333", justify="left")
        self.resultados.pack(pady=10)

    def crear_campo(self, texto, atributo):
        label = tk.Label(self.ventana, text=texto, font=("Arial", 12), bg="#f0f8ff", fg="#333")
        label.pack(pady=5)
        entrada = tk.Entry(self.ventana, font=("Arial", 12))
        entrada.pack(pady=5)
        setattr(self, f"entrada_{atributo}", entrada)

    def calcular_soluciones(self):
        try:
            a = float(self.entrada_a.get())
            b = float(self.entrada_b.get())
            c = float(self.entrada_c.get())

            if a == 0:
                messagebox.showerror("Error", "El coeficiente A no puede ser cero.")
                return

            ecuacion = EcuacionSegundoGrado(a, b, c)
            soluciones = ecuacion.calcular_soluciones()

            self.resultados.config(text=soluciones)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")


ventana_principal = tk.Tk()
app = InterfazEcuacion(ventana_principal)
ventana_principal.mainloop()
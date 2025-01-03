import tkinter as tk
from tkinter import messagebox

class ComparadorNumeros:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def comparar(self):
        if self.a > self.b:
            return f"A ({self.a}) es mayor que B ({self.b})."
        elif self.a == self.b:
            return f"A ({self.a}) es igual a B ({self.b})."
        else:
            return f"A ({self.a}) es menor que B ({self.b})."


class InterfazComparador:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Comparador de Números")
        self.ventana.geometry("400x300")
        self.ventana.configure(bg="#f0f8ff")

        titulo = tk.Label(ventana, text="Comparador de Números", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
        titulo.pack(pady=10)

        tk.Label(ventana, text="Ingrese el valor de A:", font=("Arial", 12), bg="#f0f8ff", fg="#333").pack(pady=5)
        self.entrada_a = tk.Entry(ventana, font=("Arial", 12))
        self.entrada_a.pack(pady=5)

        tk.Label(ventana, text="Ingrese el valor de B:", font=("Arial", 12), bg="#f0f8ff", fg="#333").pack(pady=5)
        self.entrada_b = tk.Entry(ventana, font=("Arial", 12))
        self.entrada_b.pack(pady=5)

        # Botón para comparar
        boton = tk.Button(ventana, text="Comparar", font=("Arial", 12), bg="#4caf50", fg="white", command=self.comparar_numeros)
        boton.pack(pady=10)

        self.resultados = tk.Label(ventana, text="", font=("Arial", 12), bg="#f0f8ff", fg="#333", justify="left")
        self.resultados.pack(pady=10)

    def comparar_numeros(self):
        try:
            a = float(self.entrada_a.get())
            b = float(self.entrada_b.get())

            comparador = ComparadorNumeros(a, b)
            mensaje = comparador.comparar()

            self.resultados.config(text=mensaje)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")


ventana_principal = tk.Tk()
app = InterfazComparador(ventana_principal)
ventana_principal.mainloop()
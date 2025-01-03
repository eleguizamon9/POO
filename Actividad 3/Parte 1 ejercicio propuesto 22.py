import tkinter as tk
from tkinter import messagebox

class Empleado:
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_mensual(self):
        return self.salario_por_hora * self.horas_trabajadas


class InterfazEmpleado:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Cálculo de Salario Mensual")
        self.ventana.geometry("500x370")
        self.ventana.configure(bg="#f0f8ff")

        titulo = tk.Label(ventana, text="Cálculo de Salario Mensual", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
        titulo.pack(pady=10)

        self.crear_campo("Nombre del empleado:", "nombre")
        self.crear_campo("Salario por hora:", "salario_hora")
        self.crear_campo("Horas trabajadas al mes:", "horas_trabajadas")

        boton = tk.Button(ventana, text="Calcular Salario", font=("Arial", 12), bg="#4caf50", fg="white",
                          command=self.calcular_salario)
        boton.pack(pady=10)

        self.resultados = tk.Label(ventana, text="", font=("Arial", 12), bg="#f0f8ff", fg="#333", justify="left")
        self.resultados.pack(pady=10)

    def crear_campo(self, texto, atributo):
        label = tk.Label(self.ventana, text=texto, font=("Arial", 12), bg="#f0f8ff", fg="#333")
        label.pack(pady=5)
        entrada = tk.Entry(self.ventana, font=("Arial", 12))
        entrada.pack(pady=5)
        setattr(self, f"entrada_{atributo}", entrada)

    def calcular_salario(self):
        try:
            nombre = self.entrada_nombre.get()
            salario_por_hora = float(self.entrada_salario_hora.get())
            horas_trabajadas = int(self.entrada_horas_trabajadas.get())

            empleado = Empleado(nombre, salario_por_hora, horas_trabajadas)
            salario_mensual = empleado.calcular_salario_mensual()

            if salario_mensual > 450000:
                mensaje = f"Nombre: {empleado.nombre}\nSalario Mensual: ${salario_mensual:,.2f}"
            else:
                mensaje = f"Nombre: {empleado.nombre}"

            self.resultados.config(text=mensaje)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos.")


ventana_principal = tk.Tk()
app = InterfazEmpleado(ventana_principal)
ventana_principal.mainloop()
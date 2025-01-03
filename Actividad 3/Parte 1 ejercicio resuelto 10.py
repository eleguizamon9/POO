import tkinter as tk
from tkinter import messagebox

class Estudiante:
    def __init__(self, numero_inscripcion, nombres, patrimonio, estrato):
        self.numero_inscripcion = numero_inscripcion
        self.nombres = nombres
        self.patrimonio = patrimonio
        self.estrato = estrato

    def calcular_pago_matricula(self):
        valor_base = 50000
        if self.patrimonio > 2000000 and self.estrato > 3:
            valor_incremento = 0.03 * self.patrimonio
            return valor_base + valor_incremento
        return valor_base


class InterfazMatricula:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Liquidación de Matrícula")
        self.ventana.geometry("500x460")
        self.ventana.configure(bg="#f0f8ff")

        titulo = tk.Label(ventana, text="Liquidación de Matrícula", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
        titulo.pack(pady=10)

        self.crear_campo("Número de inscripción:", "numero_inscripcion")
        self.crear_campo("Nombres:", "nombres")
        self.crear_campo("Patrimonio:", "patrimonio")
        self.crear_campo("Estrato social:", "estrato")

        boton = tk.Button(ventana, text="Calcular Matrícula", font=("Arial", 12), bg="#4caf50", fg="white",
                          command=self.calcular_matricula)
        boton.pack(pady=10)

        self.resultados = tk.Label(ventana, text="", font=("Arial", 12), bg="#f0f8ff", fg="#333", justify="left")
        self.resultados.pack(pady=10)

    def crear_campo(self, texto, atributo):
        label = tk.Label(self.ventana, text=texto, font=("Arial", 12), bg="#f0f8ff", fg="#333")
        label.pack(pady=5)
        entrada = tk.Entry(self.ventana, font=("Arial", 12))
        entrada.pack(pady=5)
        setattr(self, f"entrada_{atributo}", entrada)

    def calcular_matricula(self):
        try:
            numero_inscripcion = self.entrada_numero_inscripcion.get()
            nombres = self.entrada_nombres.get()
            patrimonio = float(self.entrada_patrimonio.get())
            estrato = int(self.entrada_estrato.get())

            estudiante = Estudiante(numero_inscripcion, nombres, patrimonio, estrato)
            pago_matricula = estudiante.calcular_pago_matricula()

            mensaje = (f"Número de inscripción: {estudiante.numero_inscripcion}\n"
                       f"Nombres: {estudiante.nombres}\n"
                       f"Pago de matrícula: ${pago_matricula:,.2f}")
            self.resultados.config(text=mensaje)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos.")


ventana_principal = tk.Tk()
app = InterfazMatricula(ventana_principal)
ventana_principal.mainloop()
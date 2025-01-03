import tkinter as tk
from tkinter import messagebox

class Empleado:
    def __init__(self, codigo, nombres, horas_trabajadas, valor_hora, porcentaje_retencion):
        self.codigo = codigo
        self.nombres = nombres
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora

    def calcular_salario_neto(self):
        salario_bruto = self.calcular_salario_bruto()
        return salario_bruto * (1 - self.porcentaje_retencion / 100)


class InterfazEmpleado:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Empleados")
        self.ventana.geometry("400x530")
        self.ventana.configure(bg="#f0f8ff")

        titulo = tk.Label(ventana, text="Registro de Empleados", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
        titulo.pack(pady=10)

        frame = tk.Frame(ventana, bg="#f0f8ff")
        frame.pack(pady=10)

        self.crear_campo(frame, "Código del empleado:", "codigo")
        self.crear_campo(frame, "Nombres:", "nombres")
        self.crear_campo(frame, "Horas trabajadas al mes:", "horas")
        self.crear_campo(frame, "Valor por hora trabajada:", "valor_hora")
        self.crear_campo(frame, "Porcentaje de retención (%):", "retencion")

        boton = tk.Button(ventana, text="Calcular Salario", font=("Arial", 12), bg="#4caf50", fg="white",
                          command=self.calcular_salario)
        boton.pack(pady=10)

        self.resultados = tk.Label(ventana, text="", font=("Arial", 12), bg="#f0f8ff", fg="#333", justify="left")
        self.resultados.pack(pady=10)

    def crear_campo(self, frame, texto, atributo):
        label = tk.Label(frame, text=texto, font=("Arial", 12), bg="#f0f8ff", fg="#333")
        label.pack(anchor="w", pady=2)
        entrada = tk.Entry(frame, font=("Arial", 12))
        entrada.pack(fill="x", pady=5)
        setattr(self, f"entrada_{atributo}", entrada)

    def calcular_salario(self):
        try:
            codigo = self.entrada_codigo.get()
            nombres = self.entrada_nombres.get()
            horas_trabajadas = int(self.entrada_horas.get())
            valor_hora = float(self.entrada_valor_hora.get())
            porcentaje_retencion = float(self.entrada_retencion.get())

            empleado = Empleado(codigo, nombres, horas_trabajadas, valor_hora, porcentaje_retencion)

            salario_bruto = empleado.calcular_salario_bruto()
            salario_neto = empleado.calcular_salario_neto()

            mensaje = (f"Código: {empleado.codigo}\n"
                       f"Nombres: {empleado.nombres}\n"
                       f"Salario Bruto: ${salario_bruto:,.2f}\n"
                       f"Salario Neto: ${salario_neto:,.2f}")
            self.resultados.config(text=mensaje)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos.")


ventana_principal = tk.Tk()
app = InterfazEmpleado(ventana_principal)
ventana_principal.mainloop()
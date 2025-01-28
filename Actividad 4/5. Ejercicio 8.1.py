import tkinter as tk
from tkinter import messagebox

# Clase Persona
class Persona:
    def __init__(self, nombre, apellidos, telefono, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.direccion = direccion

# Clase ListaPersonas
class ListaPersonas:
    def __init__(self):
        self.lista_personas = []

    def añadir_persona(self, persona):
        self.lista_personas.append(persona)

    def eliminar_persona(self, indice):
        if 0 <= indice < len(self.lista_personas):
            del self.lista_personas[indice]

    def borrar_lista(self):
        self.lista_personas.clear()

# Clase VentanaPrincipal
class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Personas")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.lista = ListaPersonas()

        # Etiquetas y Campos de Texto
        tk.Label(root, text="Nombre:").place(x=20, y=20)
        self.campo_nombre = tk.Entry(root)
        self.campo_nombre.place(x=100, y=20, width=150)

        tk.Label(root, text="Apellidos:").place(x=20, y=50)
        self.campo_apellidos = tk.Entry(root)
        self.campo_apellidos.place(x=100, y=50, width=150)

        tk.Label(root, text="Teléfono:").place(x=20, y=80)
        self.campo_telefono = tk.Entry(root)
        self.campo_telefono.place(x=100, y=80, width=150)

        tk.Label(root, text="Dirección:").place(x=20, y=110)
        self.campo_direccion = tk.Entry(root)
        self.campo_direccion.place(x=100, y=110, width=150)

        # Botones
        tk.Button(root, text="Añadir", command=self.añadir_persona).place(x=100, y=150, width=80)
        tk.Button(root, text="Eliminar", command=self.eliminar_nombre).place(x=20, y=330, width=80)
        tk.Button(root, text="Borrar Lista", command=self.borrar_lista).place(x=120, y=330, width=120)

        # Lista de personas
        self.lista_nombres = tk.Listbox(root, selectmode=tk.SINGLE)
        self.lista_nombres.place(x=20, y=190, width=250, height=120)

        # Barra de desplazamiento
        self.scroll_lista = tk.Scrollbar(root, orient="vertical", command=self.lista_nombres.yview)
        self.scroll_lista.place(x=270, y=190, height=120)
        self.lista_nombres.config(yscrollcommand=self.scroll_lista.set)

    def añadir_persona(self):
        persona = Persona(
            self.campo_nombre.get(),
            self.campo_apellidos.get(),
            self.campo_telefono.get(),
            self.campo_direccion.get()
        )
        self.lista.añadir_persona(persona)
        self.lista_nombres.insert(tk.END, f"{persona.nombre} - {persona.apellidos} - {persona.telefono} - {persona.direccion}")

        # Limpiar campos de texto
        self.campo_nombre.delete(0, tk.END)
        self.campo_apellidos.delete(0, tk.END)
        self.campo_telefono.delete(0, tk.END)
        self.campo_direccion.delete(0, tk.END)

    def eliminar_nombre(self):
        seleccion = self.lista_nombres.curselection()
        if seleccion:
            indice = seleccion[0]
            self.lista.eliminar_persona(indice)
            self.lista_nombres.delete(indice)
        else:
            messagebox.showerror("Error", "Debe seleccionar un elemento")

    def borrar_lista(self):
        self.lista.borrar_lista()
        self.lista_nombres.delete(0, tk.END)

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
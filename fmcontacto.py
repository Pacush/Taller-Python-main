import tkinter as tk
from tkinter import END, ttk

import contacto as cto
import dbcontacto as dbct


class VentanaUsuarios(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(width=500, height=500)
        self.title("Usuarios")

        self.label_ID = tk.Label(self, text="ID: ")
        self.label_ID.place(x=10, y=10)
        self.entry_ID = tk.Entry(self)
        self.entry_ID.place(x=10, y=40)

        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.place(x=10, y=70)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.place(x=10, y=100)

        self.label_direccion = tk.Label(self, text="Direccion: ")
        self.label_direccion.place(x=10, y=130)
        self.entry_direccion = tk.Entry(self)
        self.entry_direccion.place(x=10, y=160)

        self.btn_salvar = tk.Button(self, text="Guardar", command=lambda: self.buttonSalvar_clicked())
        self.btn_salvar.place(x=10, y=190)

        self.label_buscar_id = tk.Label(self, text="Buscar por ID: ")
        self.label_buscar_id.place(x=10, y=240)
        self.entry_buscar_id = tk.Entry(self)
        self.entry_buscar_id.place(x=10, y=270)
        self.btn_buscar_id = tk.Button(self, text="Buscar por ID", command=lambda: self.buttonBuscar_clicked())
        self.btn_buscar_id.place(x=10, y=300)

        self.dbct=dbct.dbcontacto()

    def buttonSalvar_clicked(self):
        ct_= cto.contacto()
        ct_.setID(int(self.entry_ID.get()))
        ct_.setNombre(self.entry_nombre.get())
        ct_.setDireccion(self.entry_direccion.get())

        self.dbct.salvar(ct_)

    def buttonBuscar_clicked(self):
        cto_=cto.contacto()
        cto_.setID(int(self.entry_buscar_id.get()))
        cto_= self.dbct.buscar(cto_)
        if cto is not None:
            self.entry_ID.delete(0, END)
            self.entry_ID.insert(0, str(cto_.getID()))
            self.entry_nombre.delete(0, END)
            self.entry_nombre.insert(0, str(cto_.getNombre()))
            self.entry_direccion.delete(0, END)
            self.entry_direccion.insert(0, str(cto_.getDireccion()))


app=VentanaUsuarios()
app.mainloop()

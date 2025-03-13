import tkinter as tk
from tkinter import END, Toplevel, messagebox, ttk

import dbtaller_mecanico as dbtm
import usuario as usr


class VentanaUsuarios(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(width=500, height=500)
        self.title("Usuarios")

        self.btn_ingresar = tk.Button(self, text="Ingresar usuario", command=lambda: self.buttonIngresar_clicked())
        self.btn_ingresar.place(x=10, y=10)

        self.label_buscar_id = tk.Label(self, text="Buscar por ID: ")
        self.label_buscar_id.place(x=10, y=240)
        self.entry_buscar_id = tk.Entry(self)
        self.entry_buscar_id.place(x=10, y=270)
        self.btn_buscar_id = tk.Button(self, text="Buscar por ID", command=lambda: self.buttonBuscar_clicked())
        self.btn_buscar_id.place(x=10, y=300)

        self.dbtm=dbtm.dbtaller_mecanico()

    
    def buttonIngresar_clicked(self):
        ventanaIngresarUsuario = VentanaIngresarUsuario(self)
    
    
    def buttonBuscar_clicked(self):
        pass


class VentanaIngresarUsuario(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(width=300, height=300)
        self.title("Ingresar usuario")

        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.place(x=10, y=10)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.place(x=10, y=30)

        self.label_username = tk.Label(self, text="Username: ")
        self.label_username.place(x=10, y=60)
        self.entry_username = tk.Entry(self)
        self.entry_username.place(x=10, y=80)
        
        self.label_password = tk.Label(self, text="Password: ")
        self.label_password.place(x=10, y=110)
        self.entry_password = tk.Entry(self)
        self.entry_password.place(x=10, y=140)
        
        self.label_perfil = tk.Label(self, text="Perfil: ")
        self.label_perfil.place(x=10, y=170)
        self.entry_perfil = tk.Entry(self)
        self.entry_perfil.place(x=10, y=190)

        self.btn_salvar = tk.Button(self, text="Guardar", command=lambda: self.buttonSalvar_clicked())
        self.btn_salvar.place(x=10, y=240)
        
        
    def buttonSalvar_clicked(self):
        
        if self.entry_nombre.get() == "" or self.entry_username.get() == "" or self.entry_password.get() == "" or self.entry_perfil.get() == "":
            messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro.")
            self.focus()
        else:
            
            usr_= usr.Usuario()
            usr_.setID(int(
                app.dbtm.maxSQL("usuario_id", "usuarios")[0]
            )+ 1)
            usr_.setNombre(self.entry_nombre.get())
            usr_.setUsername(self.entry_username.get())
            usr_.setPassword(self.entry_password.get())
            usr_.setPerfil(self.entry_perfil.get())
            try:
                app.dbtm.guardarUser(usr_)
                messagebox.showinfo("Registro exitoso", "Se ha guardado correctamente al usuario en los registros.")
                self.destroy()
            except:
                messagebox.showerror("Error", "Hubo un error al intentar ingresar el registro. Revisa tus datos.")
            
        

app=VentanaUsuarios()
app.mainloop()

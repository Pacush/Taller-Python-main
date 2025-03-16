import tkinter as tk
from tkinter import END, Toplevel, messagebox, ttk

import dbusuarios as dbu
import usuario as usr


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(width=500, height=500)
        self.title("Menú principal")

        self.label_titulo = tk.Label(self, text="Taller Mecánico", font=("Arial", 16, "bold"), bg="black", fg="white")
        self.label_titulo.place(x=160, y=20)
        
        #self.btn_usuarios = tk.Button(self, text="Usuarios", font=("Arial", 10, "bold"), command=lambda: ventanaTablaUsuarios())
        #self.btn_usuarios.place(x=210, y=80)
        
        self.menu_bar = tk.Menu(self)
        
        self.menu_archivo = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_archivo.add_command(label="Usuario", command=lambda: ventanaUsuarios())
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Clientes", command=lambda: print("Clientes"))
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Vehiculos", command=lambda: print("Vehiculos"))
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Reparaciones", command=lambda: print("Reparaciones"))
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Piezas", command=lambda: print("Piezas"))
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=self.quit)
        
        self.menu_bar.add_cascade(label="File", menu=self.menu_archivo)
        
        self.config(menu=self.menu_bar, bg="black")
        
        self.dbu = dbu.dbtaller_mecanico()


def ventanaTablaUsuarios():
    ventana = tk.Toplevel()
    ventana.config(width=500, height=300)
    ventana.title("Usuarios")
    
    columnas = ("ID", "Nombre", "Username", "Password", "Perfil")
    tree = ttk.Treeview(ventana, columns=columnas, show="headings")
    
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Username", text="Username")
    tree.heading("Password", text="Password")
    tree.heading("Perfil", text="Perfil")
    
    tree.column("ID", width=50)
    tree.column("Nombre", width=150)
    tree.column("Username", width=150)
    tree.column("Password", width=150)
    tree.column("Perfil", width=150)
    
    usuarios = app.dbu.obtenerUsuarios()
    for usuario in usuarios:
        tree.insert("", tk.END, values=usuario)
        
    tree.pack(pady=20, padx=10, expand=True, fill="both")
    
    
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=10)

    btn_actualizar = tk.Button(frame_botones, text="Actualizar tabla", command=lambda: actualizarTabla())
    btn_agregar = tk.Button(frame_botones, text="Agregar usuario", command=lambda: ventanaIngresarUsuario())
    btn_editar = tk.Button(frame_botones, text="Editar selección", command=lambda: ventanaEditarUsuario(tree.selection()))
    btn_eliminar = tk.Button(frame_botones, text="Eliminar selección", command=lambda: ventanaEliminarUsuario(tree.selection()))
    btn_buscar = tk.Button(frame_botones, text="Buscar por ID", command=lambda: buttonBuscar_clicked())
    entry_id_buscar = tk.Entry(frame_botones)

    btn_actualizar.pack(side="left", padx=5)
    btn_agregar.pack(side="left", padx=5)
    btn_editar.pack(side="left", padx=5)
    btn_eliminar.pack(side="left", padx=5)
    btn_buscar.pack(side="left", padx=5)
    entry_id_buscar.pack(side="left", padx=5)
    
    def actualizarTabla():
        for row in tree.get_children():
            tree.delete(row)
        usuarios = app.dbu.obtenerUsuarios()
        for usuario in usuarios:
            tree.insert("", tk.END, values=usuario)
            
    def buttonBuscar_clicked():
        try:
            usr_ = usr.Usuario()
            usr_.setID(int(entry_id_buscar.get()))
            auxUser = app.dbu.buscarUser(usr_)
            
            if auxUser:
                ventanaBusquedaUsuario(auxUser)
            else:
                messagebox.showerror("Usuario no encontrado", "El usuario no se encuentra registrado en la DB.")
            
        except:
            messagebox.showerror("Valor no válido", "Favor de ingresar un número entero para el ID.")
            
      
    def ventanaIngresarUsuario():
        ventana = tk.Toplevel()
        ventana.config(width=300, height=300)
        ventana.title("Ingresar nuevo usuario")
        label_nombre = tk.Label(ventana, text="Nombre: ")
        label_nombre.place(x=10, y=10)
        entry_nombre = tk.Entry(ventana)
        entry_nombre.place(x=10, y=30)
        label_username = tk.Label(ventana, text="Username: ")
        label_username.place(x=10, y=60)
        entry_username = tk.Entry(ventana)
        entry_username.place(x=10, y=80)

        label_password = tk.Label(ventana, text="Password: ")
        label_password.place(x=10, y=110)
        entry_password = tk.Entry(ventana)
        entry_password.place(x=10, y=140)

        label_perfil = tk.Label(ventana, text="Perfil: ")
        label_perfil.place(x=10, y=170)
        combo_perfil = ttk.Combobox(ventana, values=["Administrador","Auxliar","Mecánico"])
        combo_perfil.place(x=10, y=190)
        btn_salvar = tk.Button(ventana, text="Guardar", command=lambda: buttonSalvar_clicked())
        btn_salvar.place(x=10, y=240)


        def buttonSalvar_clicked():
            if entry_nombre.get() == "" or entry_username.get() == "" or entry_password.get() == "" or combo_perfil.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro.")
                ventana.focus()

            elif (combo_perfil.get() != "Administrador") and (combo_perfil.get() != "Auxiliar") and (combo_perfil.get() != "Mecánico"):
                messagebox.showerror("Valores inválidos", "Favor de ingresar valores adecuados.")
                print(combo_perfil.get())
                ventana.focus()
            else:
                usr_= usr.Usuario()
                max = app.dbu.maxSQL("usuario_id", "usuarios")[0]
                if not max:
                    usr_.setID(1)
                else:
                    usr_.setID(int(
                        app.dbu.maxSQL("usuario_id", "usuarios")[0]
                    )+ 1)
                usr_.setNombre(entry_nombre.get())
                usr_.setUsername(entry_username.get())
                usr_.setPassword(entry_password.get())
                usr_.setPerfil(combo_perfil.get())
                try:
                    app.dbu.guardarUser(usr_)
                    messagebox.showinfo("Registro exitoso", "Se ha guardado correctamente al usuario en los registros.")
                    ventana.destroy()
                    actualizarTabla()
                except:
                    messagebox.showerror("Error", "Hubo un error al intentar ingresar el registro. Revisa tus datos.")


    def ventanaBusquedaUsuario(auxUser: usr.Usuario):

        ventana = tk.Toplevel()
        ventana.config(width=300, height=300)
        ventana.title("Usuario encontrado")
        label_id = tk.Label(ventana, text="ID: ", font=("Arial", 10, "bold"))
        label_id.place(x=10, y=10)
        label_id_res = tk.Label(ventana, text=str(auxUser.getID()))
        label_id_res.place(x=10, y=30)

        label_nombre = tk.Label(ventana, text="Nombre: ", font=("Arial", 10, "bold"))
        label_nombre.place(x=10, y=60)
        label_nombre_res = tk.Label(ventana, text=auxUser.getNombre())
        label_nombre_res.place(x=10, y=80)

        label_username = tk.Label(ventana, text="Username: ", font=("Arial", 10, "bold"))
        label_username.place(x=10, y=110)
        label_username_res = tk.Label(ventana, text=auxUser.getUsername())
        label_username_res.place(x=10, y=130)

        label_password = tk.Label(ventana, text="Password: ", font=("Arial", 10, "bold"))
        label_password.place(x=10, y=160)
        label_password_res = tk.Label(ventana, text=auxUser.getPassword())
        label_password_res.place(x=10, y=180)

        label_perfil = tk.Label(ventana, text="Perfil: ", font=("Arial", 10, "bold"))
        label_perfil.place(x=10, y=210)
        label_perfil_res = tk.Label(ventana, text=auxUser.getPerfil())
        label_perfil_res.place(x=10, y=240)

    def ventanaEditarUsuario(seleccion: ttk.Treeview.selection):
        
        if not seleccion:
            messagebox.showerror("Sin selección", "No hay ningún elemento de la tabla seleccionado.")
            return
            
        else:
            valores = tree.item(seleccion[0], "values")
            
            ventana = tk.Toplevel()
            ventana.config(width=300, height=500)
            ventana.title("Editar usuario")

            label_id = tk.Label(ventana, text="ID: ", font=("Arial", 10, "bold"))
            label_id.place(x=10, y=10)
            label_id_res = tk.Label(ventana, text= valores[0])
            label_id_res.place(x=10, y=30)

            label_nombre = tk.Label(ventana, text="Nombre: ", font=("Arial", 10, "bold"))
            label_nombre.place(x=10, y=60)
            entry_nombre = tk.Entry(ventana)
            entry_nombre.place(x=10, y=80)

            label_username = tk.Label(ventana, text="Username: ", font=("Arial", 10, "bold"))
            label_username.place(x=10, y=110)
            entry_username = tk.Entry(ventana)
            entry_username.place(x=10, y=130)

            label_password = tk.Label(ventana, text="Password: ", font=("Arial", 10, "bold"))
            label_password.place(x=10, y=160)
            entry_password = tk.Entry(ventana)
            entry_password.place(x=10, y=180)

            label_perfil = tk.Label(ventana, text="Perfil: ", font=("Arial", 10, "bold"))
            label_perfil.place(x=10, y=210)
            combo_perfil = ttk.Combobox(ventana, values=["Administrador", "Auxiliar", "Mecánico"])
            combo_perfil.place(x=10, y=240)

            btn_guardar = tk.Button(ventana, text="Guardar", command=lambda: guardar_edicion())
            btn_guardar.place(x=10, y=290)
            
            entry_nombre.insert(0, valores[1])
            entry_username.insert(0, valores[2])
            entry_password.insert(0, valores[3])
            combo_perfil.insert(0, valores[4])
            
            def guardar_edicion():
                try:
                    
                    if entry_nombre.get() == "" or entry_username.get() == "" or entry_password.get() == "" or combo_perfil.get() == "":
                        messagebox.showerror("Campos faltantes", "Faltan campos por llenar para editar el registro.")
                        ventana.focus()
                    elif (combo_perfil.get() != "Administrador") and (combo_perfil.get() != "Auxiliar") and (combo_perfil.get() != "Mecánico"):
                        messagebox.showerror("Valores inválidos", "Favor de ingresar valores adecuados.")
                        ventana.focus()
                        print(combo_perfil.get() != "Administrador")
                    else:
                        auxUser = usr.Usuario()
                        auxUser.setID(int(label_id_res.cget("text")))
                        auxUser.setNombre(entry_nombre.get())
                        auxUser.setUsername(entry_username.get())
                        auxUser.setPassword(entry_password.get())
                        auxUser.setPerfil(combo_perfil.get())

                        edicion = app.dbu.editarUser(auxUser)
                        if edicion:
                            messagebox.showinfo("Edición exitosa", "Se han editado correctamente los datos del usuario.")
                            ventana.destroy()
                            actualizarTabla()
                        else:
                            messagebox.showerror("Edición fallida", "No ha sido posible editar los datos del usuario.")
                            ventana.destroy()
                    
                except Exception as e:
                    messagebox.showerror("Valores inválidos", "Favor de ingresar valores adecuados.")
                    ventana.focus()
                    print(e)
    
    def ventanaEliminarUsuario(seleccion: ttk.Treeview.selection):
        if not seleccion:
            messagebox.showerror("Sin selección", "No hay ningún elemento de la tabla seleccionado.")
            return
            
        else:
            valores = tree.item(seleccion[0], "values")
            confirmation = messagebox.askyesno("¿Desea continuar?", f"¿Desea eliminar al usuario con id {valores[0]}?")
            if confirmation:
                if app.dbu.eliminarUser(int(valores[0])):
                    messagebox.showinfo("Eliminación exitosa", f"Se ha eliminado satisfactoriamente al usuario con id {valores[0]}.")
                    actualizarTabla()
                else:
                    messagebox.showerror("Eliminación fallida", "No ha sido posible elimiar al usuario.")
                    
            else:
                ventana.focus()
         


def ventanaUsuarios():
    ventana = tk.Toplevel()
    ventana.config(width=500, height=500, bg="black")
    ventana.title("Usuarios")
    
    label_id_buscar = tk.Label(ventana, text="Ingrese ID a buscar:", bg="black", fg="white")
    label_id_buscar.place(x=30, y=10)
    entry_id_buscar = tk.Entry(ventana, width=30)
    entry_id_buscar.place(x=140, y=10)
    btn_id_buscar = tk.Button(ventana, text="Buscar", command=lambda: buttonBuscar_clicked(), width=10)
    btn_id_buscar.place(x=330, y=10)
    
    label_id = tk.Label(ventana, text="ID:", bg="black", fg="white")
    label_id.place(x=30, y=50)
    entry_id = tk.Entry(ventana, state="disabled")
    entry_id.place(x=100, y=50)
    
    label_nombre = tk.Label(ventana, text="Nombre:", bg="black", fg="white")
    label_nombre.place(x=30, y=80)
    entry_nombre = tk.Entry(ventana, width=50)
    entry_nombre.place(x=100, y=80)
    
    label_username = tk.Label(ventana, text="Username:", bg="black", fg="white")
    label_username.place(x=30, y=110)
    entry_username = tk.Entry(ventana, width=50)
    entry_username.place(x=100, y=110)
    
    label_password = tk.Label(ventana, text="Password:", bg="black", fg="white")
    label_password.place(x=30, y=140)
    entry_password = tk.Entry(ventana, width=30, show="*")
    entry_password.place(x=100, y=140)
    
    label_perfil = tk.Label(ventana, text="Perfil:", bg="black", fg="white")
    label_perfil.place(x=30, y=170)
    combo_perfil = ttk.Combobox(ventana, values=perfiles, width=30)
    combo_perfil.place(x=100, y=170)
    
    frame_botones = tk.Frame(ventana, bg="black")
    frame_botones.place(x=30, y=210)
    
    btn_nuevo = tk.Button(frame_botones, text="Nuevo", state="normal", command=lambda: buttonNuevo_clicked())
    btn_guardar = tk.Button(frame_botones, text="Guardar", state="disabled", command=lambda: buttonGuardar_clicked())
    btn_cancelar = tk.Button(frame_botones, text="Cancelar", state="disabled", command=lambda: buttonCancelar_clicked())
    btn_editar = tk.Button(frame_botones, text="Editar", state="disabled", command=lambda: buttonEditar_clicked())
    btn_remover = tk.Button(frame_botones, text="Remover", state="disabled", command=lambda: ventanaEliminarUsuario())
    
    btn_nuevo.pack(side="left", padx=5)
    btn_guardar.pack(side="left", padx=5)
    btn_cancelar.pack(side="left", padx=5)
    btn_editar.pack(side="left", padx=5)
    btn_remover.pack(side="left", padx=5)
    
    
    
    def buttonGuardar_clicked():
            if entry_nombre.get() == "" or entry_username.get() == "" or entry_password.get() == "" or combo_perfil.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro.")
                ventana.focus()

            elif not (combo_perfil.get() in perfiles):
                messagebox.showerror("Valores inválidos", "Favor de ingresar valores adecuados.")
                ventana.focus()
            else:
                auxUser= usr.Usuario()
                newID = int(entry_id.get())
                if not newID:
                    auxUser.setID(1)
                else:
                    auxUser.setID(newID)
                    auxUser.setNombre(entry_nombre.get())
                    auxUser.setUsername(entry_username.get())
                    auxUser.setPassword(entry_password.get())
                    auxUser.setPerfil(combo_perfil.get())
                try:
                    app.dbu.guardarUser(auxUser)
                    messagebox.showinfo("Registro exitoso", f"Se ha guardado correctamente al usuario en los registros con el ID {auxUser.getID()}.", )
                    ventana.focus()
                    
                    entry_id.config(state="normal")
                    entry_id.delete(0, END)
                    entry_id.config(state="disabled")
                    entry_nombre.delete(0, END)
                    entry_username.delete(0, END)
                    entry_password.delete(0, END)
                    combo_perfil.delete(0, END)
                    btn_guardar.config(state="disabled")
                    btn_nuevo.config(state="normal")
                    
                except Exception as e:
                    messagebox.showerror("Error", "Hubo un error al intentar ingresar el registro. Revisa tus datos.")
                    print(e)


    def buttonBuscar_clicked():
        try:
            usr_ = usr.Usuario()
            usr_.setID(int(entry_id_buscar.get()))
            auxUser = app.dbu.buscarUser(usr_)
            
            if auxUser:
                entry_id.config(state="normal")
                entry_id.delete(0, END)
                entry_id.insert(0, auxUser.getID())
                entry_id.config(state="disabled")
                entry_nombre.delete(0, END)
                entry_nombre.insert(0, auxUser.getNombre())
                entry_username.delete(0, END)
                entry_username.insert(0, auxUser.getUsername())
                entry_password.delete(0, END)
                entry_password.insert(0, auxUser.getPassword())
                combo_perfil.delete(0, END)
                combo_perfil.insert(0, auxUser.getPerfil())
                
                btn_cancelar.config(state="normal")
                btn_editar.config(state="normal")
                btn_remover.config(state="normal")
                
                
            else:
                messagebox.showerror("Usuario no encontrado", "El usuario no se encuentra registrado en la DB.")
                ventana.focus()
            
        except Exception as e:
            messagebox.showerror("Valor no válido", "Favor de ingresar un número entero en el campo 'ID'.")
            print(e)
            ventana.focus()
            
    def buttonCancelar_clicked():
        entry_id.config(state="normal")
        entry_id.delete(0, END)
        entry_id.config(state="disabled")
        entry_id_buscar.delete(0, END)
        entry_nombre.delete(0, END)
        entry_username.delete(0, END)
        entry_password.delete(0, END)
        combo_perfil.delete(0, END)
        btn_nuevo.config(state="normal")
        btn_cancelar.config(state="disabled")
        btn_editar.config(state="disabled")
        btn_remover.config(state="disabled")
        
    def buttonNuevo_clicked():
        btn_nuevo.config(state="disabled")
        newID = app.dbu.maxSQL("usuario_id", "usuarios")[0] + 1
        entry_id.config(state="normal")
        entry_id.insert(0, newID)
        entry_id.config(state="disabled")
        btn_guardar.config(state="normal")
        
    def buttonEditar_clicked():
        try:
            if entry_nombre.get() == "" or entry_username.get() == "" or entry_password.get() == "" or combo_perfil.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para editar el registro.")
                ventana.focus()
            elif not (combo_perfil.get() in perfiles):
                messagebox.showerror("Valores inválidos", "Favor de ingresar valores adecuados.")
                ventana.focus()
            else:
                auxUser = usr.Usuario()
                auxUser.setID(int(entry_id.get()))
                auxUser.setNombre(entry_nombre.get())
                auxUser.setUsername(entry_username.get())
                auxUser.setPassword(entry_password.get())
                auxUser.setPerfil(combo_perfil.get())
                edicion = app.dbu.editarUser(auxUser)
                if edicion:
                    messagebox.showinfo("Edición exitosa", "Se han editado correctamente los datos del usuario.")
                    buttonCancelar_clicked()
                    ventana.focus()
                    
                else:
                    messagebox.showerror("Edición fallida", "No ha sido posible editar los datos del usuario.")
                    ventana.focus()
                
        except Exception as e:
            messagebox.showerror("Valores inválidos", "Favor de ingresar valores adecuados.")
            ventana.focus()
            print(e)
            
    def ventanaEliminarUsuario():
        auxUsr = usr.Usuario()
        auxUsr.setID(int(entry_id.get()))
        
        confirmation = messagebox.askyesno("¿Desea continuar?", f"¿Desea eliminar al usuario con ID {auxUsr.getID()}?")
        if confirmation:
            if app.dbu.eliminarUser(auxUsr.getID()):
                messagebox.showinfo("Eliminación exitosa", f"Se ha eliminado satisfactoriamente al usuario con ID {auxUsr.getID()}.")
                buttonCancelar_clicked()
                ventana.focus()
                
            else:
                messagebox.showerror("Eliminación fallida", "No ha sido posible elimiar al usuario.")
                ventana.focus()
                
        else:
            ventana.focus()
            


perfiles = ["Administrador", "Auxiliar", "Mecanico"]
app=App()
app.mainloop()

import tkinter as tk
from tkinter import END, Toplevel, messagebox, ttk

import cliente as cli
import dbclientes as dbc
import dbusuarios as dbu
import dbvehiculos as dbv
import usuario as usr
import vehiculo as veh

perfiles = ["Administrador", "Auxiliar", "Mecanico"]

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(width=300, height=500, bg="black")
        self.title("Login")

        self.label_titulo = tk.Label(self, text="Taller Mecánico", font=("Arial", 16, "bold"), bg="black", fg="white")
        self.label_titulo.place(x=80, y=10)

        self.label_username = tk.Label(self, text="Username: ", font=("Arial", 10, "bold"), bg="black", fg="white")
        self.label_username.place(x=10, y=60)
        self.entry_username = tk.Entry(self)
        self.entry_username.place(x=100, y=60)
        self.label_password = tk.Label(self, text="Password: ", font=("Arial", 10, "bold"), bg="black", fg="white")
        self.label_password.place(x=10, y=90)
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.place(x=100, y=90)

        self.btn_login = tk.Button(self, text="Login", command=lambda:buttonLogin_clicked())
        self.btn_login.place(x=100,y=130)


        def buttonLogin_clicked():
            aux = usr.Usuario()
            aux.setUsername(self.entry_username.get())
            aux.setPassword(self.entry_password.get())

            dbus = dbu.dbusuarios()
            userLogged = dbus.autentificar(aux)

            if userLogged == 0:
                messagebox.showerror("Error", "La contraseña es incorrecta. Revisa tus datos.")
                return
            if userLogged == 1:
                messagebox.showerror("Error", "El username ingresado no existe. Revisa tus datos.")
            if userLogged:
                self.destroy()
                app=App(userLogged)
                app.mainloop()
            else:
                messagebox.showerror("Error", "Hubo un error al intentar ingresar. Revisa tus datos.")


class App(tk.Tk):

    def __init__(self, userLogged:usr.Usuario):
        super().__init__()
        self.config(width=500, height=500)
        self.title("Menú principal")

        self.label_titulo = tk.Label(self, text="Taller Mecánico", font=("Arial", 16, "bold"), bg="black", fg="white")
        self.label_titulo.place(x=160, y=20)
        
        #self.btn_usuarios = tk.Button(self, text="Usuarios", font=("Arial", 10, "bold"), command=lambda: ventanaTablaUsuarios())
        #self.btn_usuarios.place(x=210, y=80)
        
        self.menu_bar = tk.Menu(self)
        
        self.menu_archivo = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_archivo.add_command(label="Usuario", command=lambda: ventanaUsuarios(self))
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Clientes", command=lambda: ventanaClientes(self))
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Vehiculos", command=lambda: ventanaVehiculos(self))
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Reparaciones", command=lambda: print("Reparaciones"))
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Piezas", command=lambda: print("Piezas"))
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=self.quit)
        
        self.menu_bar.add_cascade(label="File", menu=self.menu_archivo)
        
        self.config(menu=self.menu_bar, bg="black")
        
        self.dbu = dbu.dbusuarios()
        self.dbc = dbc.dbclientes()
        self.dbv = dbv.dbvehiculos()

        self.userLogged = userLogged

def ventanaUsuarios(app: App):
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


def ventanaClientes(app: App):
    ventana = tk.Toplevel()
    ventana.config(width=500, height=500, bg="black")
    ventana.title("Clientes")
    
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
    
    label_rfc = tk.Label(ventana, text="RFC:", bg="black", fg="white")
    label_rfc.place(x=30, y=110)
    entry_rfc = tk.Entry(ventana, width=50)
    entry_rfc.place(x=100, y=110)
    
    label_telefono = tk.Label(ventana, text="Telefono:", bg="black", fg="white")
    label_telefono.place(x=30, y=140)
    entry_telefono = tk.Entry(ventana, width=30, show="*")
    entry_telefono.place(x=100, y=140)
    
    label_usuario_id = tk.Label(ventana, text="Usuario ID:", bg="black", fg="white")
    label_usuario_id.place(x=30, y=170)
    entry_usuario_id = tk.Entry(ventana, width=30)
    entry_usuario_id.place(x=100, y=170)
    entry_usuario_id.insert(0, app.userLogged.getID())
    entry_usuario_id.config(state="disabled")
    
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

    def buttonBuscar_clicked():
        try:
            cli_ = cli.Cliente()
            cli_.setID(int(entry_id_buscar.get()))
            auxCli = app.dbc.buscarCliente(cli_)
            
            if auxCli:
                entry_id.config(state="normal")
                entry_id.delete(0, END)
                entry_id.insert(0, auxCli.getID())
                entry_id.config(state="disabled")
                entry_nombre.delete(0, END)
                entry_nombre.insert(0, auxCli.getNombre())
                entry_rfc.delete(0, END)
                entry_rfc.insert(0, auxCli.getRfc())
                entry_telefono.delete(0, END)
                entry_telefono.insert(0, auxCli.getTelefono())
                btn_cancelar.config(state="normal")
                btn_editar.config(state="normal")
                btn_remover.config(state="normal")
                
                
            else:
                messagebox.showerror("Cliente no encontrado", "El cliente no se encuentra registrado en la DB.")
                ventana.focus()
            
        except Exception as e:
            messagebox.showerror("Valor no válido", "Favor de ingresar un número entero en el campo 'ID'.")
            print(e)
            ventana.focus()

    def buttonGuardar_clicked():
            if entry_nombre.get() == "" or entry_id.get() == "" or entry_rfc.get() == "" or entry_telefono.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro.")
                ventana.focus()
            
            else:
                auxCliente= cli.Cliente()
                newID = int(entry_id.get())
                if not newID:
                    auxCliente.setID(1)
                else:
                    auxCliente.setID(newID)
                    auxCliente.setNombre(entry_nombre.get())
                    auxCliente.setRfc(entry_rfc.get())
                    auxCliente.setTelefono(entry_telefono.get())
                    auxCliente.setUsuarioID(app.userLogged.getID())
                try:
                    app.dbc.guardarCliente(auxCliente)
                    messagebox.showinfo("Registro exitoso", f"Se ha guardado correctamente al cliente con el ID {auxCliente.getID()}. Se registra bajo el username {app.userLogged.getUsername()}", )
                    ventana.focus()
                    
                    entry_id.config(state="normal")
                    entry_id.delete(0, END)
                    entry_id.config(state="disabled")
                    entry_nombre.delete(0, END)
                    entry_rfc.delete(0, END)
                    entry_telefono.delete(0, END)
                    btn_guardar.config(state="disabled")
                    btn_nuevo.config(state="normal")
                    
                except Exception as e:
                    messagebox.showerror("Error", "Hubo un error al intentar ingresar el registro. Revisa tus datos.")
                    print(e)
    
    def buttonNuevo_clicked():
        btn_nuevo.config(state="disabled")

        max = app.dbc.maxSQL("cliente_id", "clientes")[0]
        if max == None:
            newID = 1
        else:
            newID = max + 1

        entry_id.config(state="normal")
        entry_id.insert(0, newID)
        entry_id.config(state="disabled")
        btn_guardar.config(state="normal")
        
    def buttonEditar_clicked():
        try:
            if entry_nombre.get() == "" or entry_id.get() == "" or entry_rfc.get() == "" or entry_telefono.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para editar el registro.")
                ventana.focus()

            else:
                auxCli = cli.Cliente()
                auxCli.setID(int(entry_id.get()))
                auxCli.setNombre(entry_nombre.get())
                auxCli.setRfc(entry_rfc.get())
                auxCli.setTelefono(entry_telefono.get())
                auxCli.setUsuarioID(app.userLogged.getID())
                edicion = app.dbc.editarCliente(auxCli)
                if edicion:
                    messagebox.showinfo("Edición exitosa", "Se han editado correctamente los datos del cliente.")
                    buttonCancelar_clicked()
                    ventana.focus()
                    
                else:
                    messagebox.showerror("Edición fallida", "No ha sido posible editar los datos del cliente.")
                    ventana.focus()
                
        except Exception as e:
            messagebox.showerror("Valores inválidos", "Favor de ingresar valores adecuados.")
            ventana.focus()
            print(e)

    def buttonCancelar_clicked():
        entry_id.config(state="normal")
        entry_id.delete(0, END)
        entry_id.config(state="disabled")
        entry_id_buscar.delete(0, END)
        entry_nombre.delete(0, END)
        entry_rfc.delete(0, END)
        entry_telefono.delete(0, END)
        btn_nuevo.config(state="normal")
        btn_cancelar.config(state="disabled")
        btn_editar.config(state="disabled")
        btn_remover.config(state="disabled")
        
    def ventanaEliminarUsuario():
        auxCli = cli.Cliente()
        auxCli.setID(int(entry_id.get()))
        
        confirmation = messagebox.askyesno("¿Desea continuar?", f"¿Desea eliminar al cliente con ID {auxCli.getID()}?")
        if confirmation:
            if app.dbc.eliminarCliente(auxCli.getID()):
                messagebox.showinfo("Eliminación exitosa", f"Se ha eliminado satisfactoriamente al cliente con ID {auxCli.getID()}.")
                buttonCancelar_clicked()
                ventana.focus()
                
            else:
                messagebox.showerror("Eliminación fallida", "No ha sido posible elimiar al cliente.")
                ventana.focus()
                
        else:
            ventana.focus()

def ventanaVehiculos(app: App):
    ventana = tk.Toplevel()
    ventana.config(width=500, height=500, bg="black")
    ventana.title("Vehiculos")
    
    cliNombresID = app.dbc.dictClientesId(app.userLogged.getID())
    cliNombres = []
    cliIDs = []
    for cliente in cliNombresID:
        cliIDs.append(int(cliente[0]))
        cliNombres.append(cliente[1])
    
    label_id_buscar = tk.Label(ventana, text="Ingrese matricula a buscar:", bg="black", fg="white")
    label_id_buscar.place(x=30, y=10)
    entry_id_buscar = tk.Entry(ventana, width=30)
    entry_id_buscar.place(x=140, y=10)
    btn_id_buscar = tk.Button(ventana, text="Buscar", command=lambda: buttonBuscar_clicked(), width=10)
    btn_id_buscar.place(x=330, y=10)
    
    label_matricula = tk.Label(ventana, text="Matricula:", bg="black", fg="white")
    label_matricula.place(x=30, y=50)
    entry_matricula = tk.Entry(ventana)
    entry_matricula.place(x=100, y=50)
    
    label_nombre = tk.Label(ventana, text="Cliente:", bg="black", fg="white")
    label_nombre.place(x=30, y=80)
    combo_cliente = ttk.Combobox(ventana, values=cliNombres, width=30)
    combo_cliente.place(x=100, y=80)
    
    label_marca = tk.Label(ventana, text="Marca:", bg="black", fg="white")
    label_marca.place(x=30, y=110)
    entry_marca = tk.Entry(ventana, width=50)
    entry_marca.place(x=100, y=110)
    
    label_modelo = tk.Label(ventana, text="Modelo:", bg="black", fg="white")
    label_modelo.place(x=30, y=140)
    entry_modelo = tk.Entry(ventana, width=30, show="*")
    entry_modelo.place(x=100, y=140)
    
    label_usuario_id = tk.Label(ventana, text="Usuario ID:", bg="black", fg="white")
    label_usuario_id.place(x=30, y=170)
    entry_usuario_id = tk.Entry(ventana, width=30)
    entry_usuario_id.place(x=100, y=170)
    entry_usuario_id.insert(0, app.userLogged.getID())
    entry_usuario_id.config(state="disabled")
    
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

    def buttonBuscar_clicked():
        try:
            veh_ = veh.Vehiculo()
            veh_.setMatricula(entry_id_buscar.get())
            auxVeh = app.dbv.buscarVehiculos(veh_)
            if auxVeh:
                idCliente = veh_.getClienteID()
                cliNombre = cliNombres[cliIDs.index(idCliente)]
                entry_matricula.delete(0, END)
                entry_matricula.insert(0, auxVeh.getMatricula())
                combo_cliente.delete(0, END)
                combo_cliente.insert(0, cliNombre)
                entry_marca.delete(0, END)
                entry_marca.insert(0, auxVeh.getMarca())
                entry_modelo.delete(0, END)
                entry_modelo.insert(0, auxVeh.getModelo())
                btn_cancelar.config(state="normal")
                btn_editar.config(state="normal")
                btn_remover.config(state="normal")
            else:
                messagebox.showerror("Vehiculo no encontrado", "El vehiculo no se encuentra registrado en la DB.")
                ventana.focus()
        except Exception as e:
            messagebox.showerror("Valor no válido", "Favor de ingresar una matricula válida en el campo 'Matricula'.")
            print(e)
            ventana.focus()

    def buttonGuardar_clicked():
            if entry_nombre.get() == "" or entry_id.get() == "" or entry_rfc.get() == "" or entry_telefono.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro.")
                ventana.focus()
            
            else:
                auxCliente= cli.Cliente()
                newID = int(entry_id.get())
                if not newID:
                    auxCliente.setID(1)
                else:
                    auxCliente.setID(newID)
                    auxCliente.setNombre(entry_nombre.get())
                    auxCliente.setRfc(entry_rfc.get())
                    auxCliente.setTelefono(entry_telefono.get())
                    auxCliente.setUsuarioID(app.userLogged.getID())
                try:
                    app.dbc.guardarCliente(auxCliente)
                    messagebox.showinfo("Registro exitoso", f"Se ha guardado correctamente al cliente con el ID {auxCliente.getID()}. Se registra bajo el username {app.userLogged.getUsername()}", )
                    ventana.focus()
                    
                    entry_id.config(state="normal")
                    entry_id.delete(0, END)
                    entry_id.config(state="disabled")
                    entry_nombre.delete(0, END)
                    entry_rfc.delete(0, END)
                    entry_telefono.delete(0, END)
                    btn_guardar.config(state="disabled")
                    btn_nuevo.config(state="normal")
                    
                except Exception as e:
                    messagebox.showerror("Error", "Hubo un error al intentar ingresar el registro. Revisa tus datos.")
                    print(e)
    
    def buttonNuevo_clicked():
        btn_guardar.config(state="normal")
        
    def buttonEditar_clicked():
        try:
            if entry_nombre.get() == "" or entry_id.get() == "" or entry_rfc.get() == "" or entry_telefono.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para editar el registro.")
                ventana.focus()

            else:
                auxCli = cli.Cliente()
                auxCli.setID(int(entry_id.get()))
                auxCli.setNombre(entry_nombre.get())
                auxCli.setRfc(entry_rfc.get())
                auxCli.setTelefono(entry_telefono.get())
                auxCli.setUsuarioID(app.userLogged.getID())
                edicion = app.dbc.editarCliente(auxCli)
                if edicion:
                    messagebox.showinfo("Edición exitosa", "Se han editado correctamente los datos del cliente.")
                    buttonCancelar_clicked()
                    ventana.focus()
                    
                else:
                    messagebox.showerror("Edición fallida", "No ha sido posible editar los datos del cliente.")
                    ventana.focus()
                
        except Exception as e:
            messagebox.showerror("Valores inválidos", "Favor de ingresar valores adecuados.")
            ventana.focus()
            print(e)

    def buttonCancelar_clicked():
        entry_id.config(state="normal")
        entry_id.delete(0, END)
        entry_id.config(state="disabled")
        entry_id_buscar.delete(0, END)
        entry_nombre.delete(0, END)
        entry_rfc.delete(0, END)
        entry_telefono.delete(0, END)
        btn_nuevo.config(state="normal")
        btn_cancelar.config(state="disabled")
        btn_editar.config(state="disabled")
        btn_remover.config(state="disabled")
        
    def ventanaEliminarUsuario():
        auxCli = cli.Cliente()
        auxCli.setID(int(entry_id.get()))
        
        confirmation = messagebox.askyesno("¿Desea continuar?", f"¿Desea eliminar al cliente con ID {auxCli.getID()}?")
        if confirmation:
            if app.dbc.eliminarCliente(auxCli.getID()):
                messagebox.showinfo("Eliminación exitosa", f"Se ha eliminado satisfactoriamente al cliente con ID {auxCli.getID()}.")
                buttonCancelar_clicked()
                ventana.focus()
                
            else:
                messagebox.showerror("Eliminación fallida", "No ha sido posible elimiar al cliente.")
                ventana.focus()
                
        else:
            ventana.focus()



login=Login()
login.mainloop()
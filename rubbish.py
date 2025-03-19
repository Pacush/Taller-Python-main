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
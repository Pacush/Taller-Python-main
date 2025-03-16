import conexion as con
import usuario as usr


class dbtaller_mecanico:
    
    def obtenerUsuarios(self):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "select * from usuarios"
        self.cursor1.execute(self.sql)
        rows = self.cursor1.fetchall()
        return rows
    
    
    def guardarUser(self, usr: usr.Usuario):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "insert into usuarios (usuario_id, nombre, username, password, perfil) values (%s, %s, %s, %s, %s)"
        self.datos=(usr.getID(),
                    usr.getNombre(),
                    usr.getUsername(),
                    usr.getPassword(),
                    usr.getPerfil())
        self.cursor1.execute(self.sql, self.datos)
        self.conn.commit()
        self.conn.close()


    def buscarUser(self, usr: usr.Usuario):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "select * from usuarios where usuario_id={}".format(usr.getID())
        self.cursor1.execute(self.sql)
        aux = None
        row = self.cursor1.fetchone()
        if row is not None:
            aux = usr
            aux.setID(int(row[0]))
            aux.setNombre(row[1])
            aux.setUsername(row[2])
            aux.setPassword(row[3])
            aux.setPerfil(row[4])
        return aux
    
    
    def editarUser(self, usr: usr.Usuario):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "UPDATE usuarios SET nombre = %s, username = %s, password = %s, perfil = %s WHERE usuario_id = %s"
            valores = (usr.getNombre(), usr.getUsername(), usr.getPassword(), usr.getPerfil(), usr.getID())
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    def eliminarUser(self, id: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "DELETE FROM usuarios WHERE usuario_id = %s"
            valores = (id,)
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def maxSQL(self, columna: str, tabla: str):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = f"SELECT MAX({columna}) FROM {tabla}"
        self.cursor1.execute(self.sql)
        row=self.cursor1.fetchone()
        self.con.close()
        return row
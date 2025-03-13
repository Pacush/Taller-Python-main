import conexion as con
import usuario as usr


class dbtaller_mecanico:
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

    def buscar(self, usr: usr.Usuario):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "select * from contactos where id={}".format(usr.getID())
        self.cursor1.execute(self.sql)
        aux = None
        row = self.cursor1.fetchone()
        if row is not None:
            aux = usr.Usuario()
            print(row[0])
            print(int(row[0]))
            aux.setID(int(row[0]))
            aux.setNombre(row[1])
            aux.setDireccion(row[2])
        return aux
    
    def maxSQL(self, columna: str, tabla: str):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = f"SELECT MAX({columna}) FROM {tabla}"
        self.cursor1.execute(self.sql)
        row=self.cursor1.fetchone()
        self.con.close()
        return row
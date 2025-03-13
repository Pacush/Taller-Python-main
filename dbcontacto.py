import conexion as con
import contacto as cto

class dbcontacto:
    def salvar(self, contacto):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "insert into contactos (id, nombre, direccion) values (%s, %s, %s)"
        self.datos=(contacto.getID(),
                    contacto.getNombre(),
                    contacto.getDireccion())
        self.cursor1.execute(self.sql, self.datos)
        self.conn.commit()
        self.conn.close()

    def buscar(self, contacto):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "select * from contactos where id={}".format(contacto.getID())
        self.cursor1.execute(self.sql)
        aux = None
        row = self.cursor1.fetchone()
        if row is not None:
            aux = cto.contacto()
            print(row[0])
            print(int(row[0]))
            aux.setID(int(row[0]))
            aux.setNombre(row[1])
            aux.setDireccion(row[2])
        return aux
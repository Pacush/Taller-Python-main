import conexion as con
import cliente as cli

class dbclientes:
    def guardarCliente(self, cli: cli.Cliente):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "insert into clientes (cliente_id, usuario_id, nombre, rfc, telefono) values (%s, %s, %s, %s, %s)"
        self.datos=(cli.getID(),
                    cli.getUsuarioID(),
                    cli.getNombre(),
                    cli.getRfc(),
                    cli.getTelefono())
        self.cursor1.execute(self.sql, self.datos)
        self.conn.commit()
        self.conn.close()

    def maxSQL(self, columna: str, tabla: str):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = f"SELECT MAX({columna}) FROM {tabla}"
        self.cursor1.execute(self.sql)
        row=self.cursor1.fetchone()
        self.con.close()
        return row
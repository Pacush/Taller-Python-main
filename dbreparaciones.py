import reparacion as rep
import conexion as con


class dbreparaciones:
    def guardarReparacion(self, rep: rep.Reparacion):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "INSERT INTO reparaciones (folio, matricula, fecha_entrada, fecha_salida, usuario_id) values (%s, %s, %s, %s, %s)"
        self.datos=(rep.getFolio(),
                    rep.getMatricula(),
                    rep.getFechaEntrada(),
                    rep.getFechaSalida(),
                    rep.getUsuarioID())
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
    
    def buscarReparacion(self, rep: rep.Reparacion, usrLogged: list):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        if usrLogged[1] == "Administrador":
            self.sql = "SELECT * FROM reparaciones where folio=%s"
            self.datos=(rep.getFolio(),)
        else:
            self.sql = "SELECT * FROM reparaciones where folio=%s AND usuario_id =%s"
            self.datos=(rep.getFolio(), usrLogged[0])
        self.cursor1.execute(self.sql, self.datos)
        aux = None
        row = self.cursor1.fetchone()
        if row is not None:
            aux = rep
            aux.setID(int(row[0]))
            aux.setUsuarioID(int(row[1]))
            aux.setNombre(row[2])
            aux.setRfc(row[3])
            aux.setTelefono(row[4])
        return aux
    
    def editarCliente(self, cli: cli.Cliente):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "UPDATE clientes SET nombre = %s, rfc = %s, telefono = %s WHERE cliente_id = %s"
            valores = (cli.getNombre(), cli.getRfc(), cli.getTelefono(), cli.getID())
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            self.con.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    def eliminarCliente(self, id: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "DELETE FROM clientes WHERE cliente_id = %s"
            valores = (id,)
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    def dictPiezasId(self):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "SELECT pieza_id, descripcion FROM piezas"
            self.cursor1.execute(self.sql)
            rows = self.cursor1.fetchall()
            return rows
        except Exception as e:
            print(e)
            return False

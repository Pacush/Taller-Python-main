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
            aux.setFolio(int(row[0]))
            aux.setMatricula(row[1])
            aux.setFechaEntrada(row[2])
            aux.setFechaSalida(row[3])
            aux.setUsuarioID(int(row[4]))
        return aux
    
    def editarReparacion(self, rep: rep.Reparacion):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "UPDATE reparaciones SET matricula = %s, fecha_entrada = %s, fecha_salida = %s WHERE folio = %s"
            valores = (rep.getMatricula(), rep.getFechaEntrada(), rep.getFechaSalida(), rep.getFolio())
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            self.con.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    def eliminarReparacion(self, folio: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "DELETE FROM reparaciones WHERE folio = %s"
            valores = (folio,)
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
        
    def detallesRep(self, folio: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "SELECT * FROM detalle_reparacion WHERE folio = %s"
            valores = (folio,)
            self.cursor1.execute(self.sql, valores)
            rows = self.cursor1.fetchall()
            return rows
        except Exception as e:
            print(e)
            return False

    def guardarDetalleReparacion(self, detalle_rep: list):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "INSERT INTO detalle_reparacion (detalle_id, folio, pieza_id, cantidad) values (%s, %s, %s, %s)"
        self.datos=(detalle_rep[0],
                    detalle_rep[1],
                    detalle_rep[2],
                    detalle_rep[3])
        self.cursor1.execute(self.sql, self.datos)
        self.conn.commit()
        self.conn.close()
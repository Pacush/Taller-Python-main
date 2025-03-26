import pieza as piz
import conexion as con


class dbpiezas:
    def guardarPieza(self, piz: piz.Pieza):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "insert into piezas (pieza_id, descripcion, existencia, precio) values (%s, %s, %s, %s)"
        self.datos=(piz.getID(),
                    piz.getDescripcion(),
                    piz.getExistencia(),
                    piz.getPrecio())
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
    
    def buscarPieza(self, piz: piz.Pieza, usrLogged: list = []):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "select * from piezas where pieza_id=%s"
        self.datos=(piz.getID(), )
        self.cursor1.execute(self.sql, self.datos)
        aux = None
        row = self.cursor1.fetchone()
        if row is not None:
            aux = piz
            aux.setID(int(row[0]))
            aux.setDescripcion(row[1])
            aux.setExistencia(int(row[2]))
            aux.setPrecio(row[3])
        return aux
    
    def editarPieza(self, piz: piz.Pieza):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "UPDATE piezas SET descripcion = %s, existencia = %s, precio = %s WHERE pieza_id = %s"
            valores = (piz.getDescripcion(), piz.getExistencia(), piz.getPrecio(), piz.getID())
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            self.con.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    def eliminarPieza(self, id: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "DELETE FROM piezas WHERE pieza_id = %s"
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

import vehiculo as veh
import conexion as con


class dbvehiculos:
    def guardarVehiculos(self, veh: veh.Vehiculo):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "insert into clientes (cliente_id, usuario_id, nombre, rfc, telefono) values (%s, %s, %s, %s, %s)"
        self.datos=(veh.getID(),
                    veh.getUsuarioID(),
                    veh.getNombre(),
                    veh.getRfc(),
                    veh.getTelefono())
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
    
    def buscarVehiculos(self, veh: veh.Vehiculo):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "select * from clientes where cliente_id={}".format(veh.getID())
        self.cursor1.execute(self.sql)
        aux = None
        row = self.cursor1.fetchone()
        if row is not None:
            aux = veh
            aux.setID(int(row[0]))
            aux.setUsuarioID(int(row[1]))
            aux.setNombre(row[2])
            aux.setRfc(row[3])
            aux.setTelefono(row[4])
        return aux
    
    def editarVehiculos(self, veh: veh.Vehiculo):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "UPDATE clientes SET nombre = %s, rfc = %s, telefono = %s WHERE cliente_id = %s"
            valores = (veh.getNombre(), veh.getRfc(), veh.getTelefono(), veh.getID())
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
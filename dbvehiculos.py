import conexion as con
import vehiculo as veh


class dbvehiculos:
    def guardarVehiculo(self, veh: veh.Vehiculo):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "INSERT INTO vehiculos (matricula, cliente_id, marca, modelo, usuario_id) VALUES (%s, %s, %s, %s, %s)"
        self.datos=(veh.getMatricula(),
                    veh.getClienteID(),
                    veh.getMarca(),
                    veh.getModelo(),
                    veh.getUsuarioID())
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
        self.sql = f"select * from vehiculos where matricula='{veh.getMatricula()}'"
        self.cursor1.execute(self.sql)
        aux = None
        row = self.cursor1.fetchone()
        if row is not None:
            aux = veh
            aux.setMatricula(row[0])
            aux.setClienteID(int(row[1]))
            aux.setMarca(row[2])
            aux.setModelo(row[3])
            aux.setUsuarioID(int(row[4]))
        return aux
    
    def editarVehiculos(self, veh: veh.Vehiculo, matriculaOriginal: str):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "UPDATE vehiculos SET matricula = %s, cliente_id = %s, marca = %s, modelo = %s WHERE matricula = %s"
            print(matriculaOriginal)
            print([veh.getMatricula(), veh.getClienteID(), veh.getMarca(), veh.getModelo(), veh.getUsuarioID()])
            valores = (veh.getMatricula(), veh.getClienteID(), veh.getMarca(), veh.getModelo(), matriculaOriginal)
            
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            self.con.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    def eliminarVehiculo(self, matricula: str):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "DELETE FROM vehiculos WHERE matricula = %s"
            valores = (matricula,)
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
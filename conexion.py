import mysql.connector

class conexion:
    def __init__(self):
        self.user="root"
        self.password=""
        self.database="dbtaller_mecanico"
        self.host="localhost"

    def open(self):
        self.conn=mysql.connector.connect(host=self.host,
                                          user=self.user,
                                          passwd=self.password,
                                          database=self.database)
        return self.conn

    def close(self):
        self.conn.close()

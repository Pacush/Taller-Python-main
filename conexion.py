import mysql.connector


class conexion:
    def __init__(self):
        self.user="root"
        self.password=""
        self.database="dbtaller_mecanico"
        self.host="localhost"
        self.port="3306"

    def open(self):
        self.conn=mysql.connector.connect(host=self.host,
                                          user=self.user,
                                          passwd=self.password,
                                          database=self.database,
                                          port=self.port)
        return self.conn

    def close(self):
        self.conn.close()

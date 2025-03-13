import conexion as con
import dbcontacto


class contacto:
    def __init__(self):
        self.id=0
        self.nombre=""
        self.direccion=""

    def setID(self, id):
        self.id=id

    def getID(self):
        return self.id
    
    def setNombre(self, nombre):
        self.nombre=nombre

    def getNombre(self):
        return self.nombre
    
    def setDireccion(self, direccion):
        self.direccion=direccion

    def getDireccion(self):
        return self.direccion
    
    



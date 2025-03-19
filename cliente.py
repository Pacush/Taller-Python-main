import conexion as con
import dbclientes

class Cliente:
    def __init__(self):
        self.id=0
        self.usuario_id=""
        self.nombre=""
        self.rfc=""
        self.telefono=""

    def setID(self, id):
        self.id=id

    def getID(self):
        return self.id
    
    def setUsuarioID(self, usuario_id):
        self.usuario_id=usuario_id

    def getUsuarioID(self):
        return self.usuario_id
    
    def setNombre(self, nombre):
        self.nombre=nombre

    def getNombre(self):
        return self.nombre
    
    def setRfc(self, rfc):
        self.rfc=rfc

    def getRfc(self):
        return self.rfc
    
    def setTelefono(self, telefono):
        self.telefono=telefono

    def getTelefono(self):
        return self.telefono





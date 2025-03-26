import conexion as con


class Usuario:
    def __init__(self):
        self.id=0
        self.nombre=""
        self.username=""
        self.password=""
        self.perfil=""

    def setID(self, id):
        self.id=id

    def getID(self):
        return self.id
    
    def setNombre(self, nombre):
        self.nombre=nombre

    def getNombre(self):
        return self.nombre
    
    def setUsername(self, username):
        self.username=username

    def getUsername(self):
        return self.username
    
    def setPassword(self, password):
        self.password=password

    def getPassword(self):
        return self.password
    
    def setPerfil(self, perfil):
        self.perfil=perfil

    def getPerfil(self):
        return self.perfil
    
    

        


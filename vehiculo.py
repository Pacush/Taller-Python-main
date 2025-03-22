class Vehiculo:
    def __init__(self):
        self.matricula=""
        self.cliente_id=0
        self.marca=""
        self.modelo=""
        self.usuario_id=0

    def setMatricula(self, matricula):
        self.matricula=matricula

    def getMatricula(self):
        return self.matricula
    
    def setClienteID(self, cliente_id):
        self.cliente_id=cliente_id

    def getClienteID(self):
        return self.cliente_id
    
    def setMarca(self, marca):
        self.marca=marca

    def getMarca(self):
        return self.marca
    
    def setModelo(self, modelo):
        self.modelo=modelo

    def getModelo(self):
        return self.modelo
    
    def setUsuarioID(self, usuario_id):
        self.usuario_id=usuario_id

    def getUsuarioID(self):
        return self.usuario_id


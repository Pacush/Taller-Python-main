class Reparacion:
    def __init__(self):
        self.folio=0
        self.matricula=""
        self.fecha_entrada=""
        self.fecha_salida=""
        self.usuario_id=0

    
    def setFolio(self, folio):
        self.folio=folio

    def getFolio(self):
        return self.folio
    
    def setMatricula(self, matricula):
        self.matricula=matricula

    def getMatricula(self):
        return self.matricula
    
    def setFechaEntrada(self, fecha_entrada):
        self.fecha_entrada=fecha_entrada

    def getFechaEntrada(self):
        return self.fecha_entrada
    
    def setFechaSalida(self, fecha_salida):
        self.fecha_salida=fecha_salida

    def getFechaSalida(self):
        return self.fecha_salida

    def setUsuarioID(self, usuario_id):
        self.usuario_id=usuario_id

    def getUsuarioID(self):
        return self.usuario_id



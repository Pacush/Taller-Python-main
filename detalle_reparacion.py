class DetalleReparacion:
    def __init__(self):
        self.id=0
        self.folio=0
        self.pieza_id=0
        self.cantidad=0

    def setID(self, id):
        self.id=id

    def getID(self):
        return self.id
    
    def setFolio(self, folio):
        self.folio=folio

    def getFolio(self):
        return self.folio
    
    def setPiezaid(self, piezaid):
        self.piezaid=piezaid

    def getPiezaid(self):
        return self.piezaid
    
    def setCantidad(self, cantidad):
        self.cantidad=cantidad

    def getCantidad(self):
        return self.cantidad




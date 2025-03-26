class Pieza:
    def __init__(self):
        self.id=0
        self.descripcion=""
        self.existencia=0
        self.precio=0.0

    def setID(self, id):
        self.id=id

    def getID(self):
        return self.id
    
    def setDescripcion(self, descripcion):
        self.descripcion=descripcion

    def getDescripcion(self):
        return self.descripcion
    
    def setExistencia(self, existencia):
        self.existencia=existencia

    def getExistencia(self):
        return self.existencia
    
    def setPrecio(self, precio):
        self.precio=precio

    def getPrecio(self):
        return self.precio




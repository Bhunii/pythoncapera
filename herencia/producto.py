class Producto:
    def __init__(self, identificador, nombre, tipo, precio):
        self.__identificador=identificador
        self.__nombre=nombre
        self.__tipo=tipo
        self.__precio=precio
    
    def setIdentificador(self, identificador):
        self.__identificador=identificador
    
    def getIdentificador(self):
        return self.__identificador
    
    def setNombre(self, nombre):
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre
    
    def setTipo(self, tipo):
        self.__tipo=tipo

    def getTipo(self):
        return self.__tipo
    
    def setPrecio(self,precio):
        self.__precio(precio)
    
    def getPrecio(self):
        return self.__precio
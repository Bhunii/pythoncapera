from Cliente import *
from producto import *

class empresa(Cliente):
    def __init__(self, identificador, tipo, nombre, telefono):
        super().__init__(identificador, tipo)
        self.__nombre=nombre
        self.__telefono=telefono
        self.__producto=[]
    
    def setNombre(self, nombre):
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre
    
    def setTelefono(self, telefono):
        self.__telefono=telefono

    def getTelefono(self):
        return self.__telefono
    
    def setProducto(self,producto):
        self.__producto.append(producto)
  
    def getProducto(self):
        return self.__producto
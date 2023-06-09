class Cliente():
    def __init__ (self, identificador, tipo):
        self.__identificador=identificador
        self.__tipo=tipo
       

    def setIdentificador(self, identificador):
        self.__identificador=identificador
    
    def getIdentificador(self):
        return self.__identificador
    
    def setTipo(self, tipo):
        self.__tipo=tipo

    def getTipo(self):
        return self.__tipo
       
    
    
    
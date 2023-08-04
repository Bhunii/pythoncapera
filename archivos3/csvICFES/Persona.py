class Persona:
    def __init__(self, identificador, genero, puntaje_lectura, puntaje_matematicas, puntaje_naturales, puntaje_ingles):
        self.__identificador=identificador
        self.__genero=genero
        self.__puntaje_lectura=int(puntaje_lectura)
        self.__puntaje_matematicas=int(puntaje_matematicas)
        self.__puntaje_naturales=int(puntaje_naturales)
        self.__puntaje_ingles=int(puntaje_ingles)
    
    def verDatos(self):
        return f"{self.__identificador} {self.__genero} {self.__puntaje_lectura} {self.__puntaje_matematicas} {self.__puntaje_naturales} {self.__puntaje_ingles}"
    
    def getIdentificador(self):
        return self.__identificador
    
    def getGenero(self):
        return self.__genero
    
    def getPuntajeLectura(self):
        return self.__puntaje_lectura
    
    def getPuntajeMatematicas(self):
        return self.__puntaje_matematicas
    
    def getPuntajeNaturales(self):
        return self.__puntaje_naturales
    
    def getPuntajeIngles(self):
        return self.__puntaje_ingles
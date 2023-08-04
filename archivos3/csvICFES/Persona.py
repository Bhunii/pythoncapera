class Persona:
    def __init__(self, identificador, genero, puntaje_lectura, puntaje_matematicas, puntaje_naturales, puntaje_ingles):
        self.__identificador=identificador
        self.__genero=genero
        self.__puntaje_lectura=puntaje_lectura
        self.__puntaje_matematicas=puntaje_matematicas
        self.__puntaje_naturales=puntaje_naturales
        self.__puntaje_ingles=puntaje_ingles
    
    def verDatos(self):
        return f"{self.__identificador} {self.__genero} {self.__puntaje_lectura} {self.__puntaje_matematicas} {self.__puntaje_naturales} {self.__puntaje_ingles}"
    
    def getGenero(self):
        return self.__genero
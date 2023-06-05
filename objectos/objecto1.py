class Persona:
    def __init__(self, nombre, documento, cursos):
        self.__nombre=nombre
        self.__documento=documento
        self.__cursos=[]

    def getNombre (self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre=nombre
    
    def getDocumento (self):
        return self.__documento
    
    def setDocumento(self, documento):
        self.__documento=documento

    def getDatos (self):
        return f'{self.__nombre} , {self.__documento}'
    
    def setCursos (aux):
        (self.__cursos).append(aux)

p=Persona ('Ana',123)
# print(p.getNombre())
p.setNombre("Leidy")
print(p.getNombre())
q=Persona('Pedro',321)
# print(q.getNombre())
q.setNombre("Refisal")
print(q.getNombre())
print(q.getDatos())
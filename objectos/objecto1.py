class Persona:
    def __init__(self, nombre, documento, curso):
        self.__nombre=nombre
        self.__documento=documento
        self.__cursos=[curso]

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
    
    def setCursos (self, curso):
        self.__cursos.append(curso)
        
    def setEliminarCurso(self, aux1):
        if aux1 in self.__cursos:
            self.__cursos.remove(aux1)
    
    def setBuscarCurso(self, aux1, aux2):
        if aux1 in self.__cursos:
            

    def getCursos (self):
        return self.__cursos
    
p=Persona ('Ana',123,'Ingles')
print(p.getCursos())
p.setCursos('Ciencias')
print(p.getCursos())
p.setEliminarCurso('Ingles')
print(p.getCursos())
# print(p.getNombre())
# p.setNombre("Leidy")
# print(p.getNombre())
# q=Persona('Pedro',321)
# print(q.getNombre())
# q.setNombre("Refisal")
# print(q.getNombre())
# print(q.getDatos())
# aux1=input('ingrese un curso: ')
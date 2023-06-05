class Persona:
    lista1=[]

    def __init__(self, nombre, documento, curso):
        self.__nombre=nombre
        self.__documento=documento
        self.__cursos=[curso]
        Persona.lista1
        
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
    
    def setModificarCurso(self, aux1, aux2):
        for i in range(len(self.__cursos)):
            if self.__cursos[i] == aux1:
                self.__cursos[i] = aux2
            # else:
            #     print('curso no esta')
            # if aux1 in self.__cursos:
            # self.__cursos=aux1

    def getCursos (self):
        return self.__cursos
    
    def BuscarCurso (self, curso):
        if curso in self.__cursos:
            return (f'si esta el curso {curso}')
        else:
            return (f'no esta el curso {curso}')

    def copiarLista(self):
        lista1=self.__cursos.copy()
        print(lista1)

    # def listagen(self):
    #     persona
    
p=Persona ('Ana',123,'Ingles')
#print(p.getCursos())
p.setCursos('Ciencias')
print(p.getCursos())
# p.setEliminarCurso('Ingles')
# print(p.getCursos())
# p.setModificarCurso('Ciencias','CienciasNaturales')
# print(p.getCursos())
# print(p.BuscarCurso('CienciasNaturales'))
k=Persona ('Pedro',1333,'Python')
k.setCursos('Css')
print(k.getCursos())
print(Persona.copiarLista)

# print(p.getNombre())
# p.setNombre("Leidy")
# print(p.getNombre())
# q=Persona('Pedro',321)
# print(q.getNombre())
# q.setNombre("Refisal")
# print(q.getNombre())
# print(q.getDatos())
# aux1=input('ingrese un curso: ')

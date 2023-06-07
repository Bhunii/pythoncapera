class Empleado:
    contador=0
    suma=0

    def __init__(self, nombre, cargo ,salario, dias):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario
        self.__dias=dias
        Empleado.contador+=1
        Empleado.suma+=self.__salario
    
    def setNombre(self, nombre):
        self.__nombre=nombre

    def getNombre (self):
        return self.__nombre
        
    def setCargo (self, cargo):
        self.__cargo=cargo
    
    def getCargo (self):
        return self.__cargo
    
    def setSalario (self, salario):
        self.__salario=salario
    
    def getSalario (self):
        return self.__salario
    
    def setDias (self, dias):
        self.__dias=dias
    
    def getDias (self):
        return self.__dias
    
    def Horas (self):
        aux=round(float(self.__salario/(self.__dias*8)),5)
        return aux
    
    def setSalarioIpc (self):
        ipc=12.82
        if self.__salario >= 1160000:
            incremento=(self.__salario*ipc+3)/100
            self.__salario=self.__salario+incremento
        else:
            incremento=(self.__salario*ipc)/100
            self.__salario=self.__salario+incremento
    
    def getSalarioIpc (self):
        return self.__salario
    
    def setHorasExtras (self, extras):
        aux=self.getDias()*2
        if extras < aux:
            self.__salario=int(self.__salario+(self.Horas()*extras))
 
    def getHorasExtras (self):
        return self.__salario
    
    def mostrarSuma ():
        return Empleado.suma
    
    def promedioSalarios():
        prom=round(Empleado.suma/Empleado.contador,3)
        return prom

p=Empleado('Paola','Recepcionista',1160000,22)
# print(k.getNombre())
# print(k.getCargo())
# print(k.getSalario())
# print(k.getDias())
# print(k.Horas())
# k.setSalarioIpc()
# print(k.getSalarioIpc())
# k.setHorasExtras(40)
# print(k.getHorasExtras())

l=Empleado('Liliana','Asesora',1180000,22)
# print(l.getNombre())
# print(l.getCargo())
# print(l.getSalario())
# print(l.getDias())
# print(l.Horas())
# l.setSalarioIpc()
# print(l.getSalarioIpc())
# l.setHorasExtras(40)
# print(l.getHorasExtras())

s=Empleado('Stuart','Asesor',1180000,22)
# print(s.getNombre())
# print(s.getCargo())
# print(s.getSalario())
# print(s.getDias())
# print(s.Horas())
# s.setSalarioIpc()
# print(s.getSalarioIpc())
# s.setHorasExtras(40)
# print(s.getHorasExtras())

# print(Empleado.suma)
print(Empleado.mostrarSuma())
print(Empleado.promedioSalarios())
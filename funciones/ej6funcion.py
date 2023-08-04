import random

def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def abajoArriba(lista):
    j=promedioLista(lista)
    estado=[]
    for i in range(len(lista)):
        if lista[i] > j:
            estado.append('arriba')
        elif lista[i] < j:
            estado.append('abajo')
        else:
            estado.append('igual')
    return estado

l1=llenarLista(10,20)
print(l1)
print(promedioLista(l1))
print(abajoArriba(l1))
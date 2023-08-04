import random

def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaPares(lista):
    suma=0
    for i in lista:
        if i%2==0:
            suma+=i
    return suma

def promedioImpares(lista):
    aux=0
    cant=0
    for i in lista:
        if i%2!=0:
            aux+=i
            cant+=1
    prom=round(aux/cant, 3)
    return prom

l1=llenarLista(10,20)
print(l1)
print(sumaPares(l1))
print(promedioImpares(l1))
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

def menorLista(lista):
    menor = 1000000
    for i in lista:
        if i < menor:menor=i
    return menor

def mayorLista(lista):
    mayor=0
    for i in lista:
        if i>mayor:mayor=i
    return mayor

def ordenAscendente(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    return lista 


def ordenDescendente(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]<lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    return lista

def medianaLista(lista):
    m=ordenAscendente(lista)
    if len(lista)%2 == 0:
        y = (len(lista) // 2) 
        j = y-1
        med = (m[y] + m[j]) / 2
    else:
        med=len(lista)//2
    return lista[med]

l1=llenarLista(5,20)
print(l1)
print(sumaLista(l1))
print(promedioLista(l1))
print(menorLista(l1))
print(mayorLista(l1))
print(ordenAscendente(l1))
print(ordenDescendente(l1))
print(medianaLista(l1))
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

def sumaMayor(lista, lista1):
    for i in lista:
        sum1=sumaLista(lista)
        sum2=sumaLista(lista1)
        if sum1>sum2:
            res=sum1
        else:
            res=sum2
        return res

def mayorLista(lista):
    mayor=0
    for i in lista:
        if i>mayor:
            mayor=i
    return mayor

def menorLista(lista):
    menor = 1000000
    for i in lista:
        if i < menor:
            menor=i
    return menor

def compararMayor(lista, lista1):
    aux1=mayorLista(lista)
    aux2=mayorLista(lista1)
    if aux1>aux2:
        mayor=aux1
    elif aux2>aux1:
        mayor=aux2
    else:
        mayor=f'{aux1} estan en ambas listas'
    return mayor

def compararMenor(lista, lista1):
    aux1=menorLista(lista)
    aux2=menorLista(lista1)
    if aux1<aux2:
        mayor=aux1
    elif aux2<aux1:
        mayor=aux2
    else:
        mayor=f'{aux1} estan en ambas listas'
    return mayor

def promedioConjunto(lista, lista1):
    prom=(sumaLista(lista)+sumaLista(lista1))/(len(lista)+len(lista1))
    return prom

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def abajoOarriba(lista,lista1):
    aux=[]
    aux.append(promedioLista(lista))
    aux.append(promedioLista(lista1))
    s=promedioConjunto(lista, lista1)
    estado=[]
    for i in range(len(aux)):
        if aux[i] > s:
            estado.append('arriba')
        elif aux[i] < s:
            estado.append('abajo')
        else:
            estado.append('igual')
    return estado

def paresLista(lista):
    par=0
    for i in lista:
        if i%2==0:
            par+=1
    return par

def compararParesLista(lista, lista1):
    aux1=paresLista(lista)
    aux2=paresLista(lista1)
    if aux1 > aux2:
        res=aux1
    if aux2 > aux1:
        res=aux2
    if aux1 == aux2:
        res=f'son iguales ({aux1})'
    return res

def imparesLista(lista):
    impar=0
    for i in lista:
        if i%2!=0:
            impar+=1
    return impar

def compararImparesLista(lista, lista1):
    aux1=imparesLista(lista)
    aux2=imparesLista(lista1)
    if aux1 > aux2:
        res=aux1
    if aux2 > aux1:
        res=aux2
    if aux1 == aux2:
        res=f'son iguales ({aux1})'
    return res

l1=llenarLista(10,20)
l2=llenarLista(10,20)
print(l1)
print(l2)
# print(sumaLista(l1))
# print(sumaLista(l2))
print(sumaMayor(l1, l2))
# print(mayorLista(l1))
# print(mayorLista(l2))
print(compararMayor(l1,l2))
# print(menorLista(l1))
# print(menorLista(l2))
print(compararMenor(l1, l2))
# print(sumaLista(l1))
# print(sumaLista(l2))
print(promedioConjunto(l1,l2))
# print(promedioLista(l1))
# print(promedioLista(l2))
print(abajoOarriba(l1,l2))
# print(paresLista(l1))
# print(paresLista(l2))
print(compararParesLista(l1,l2))
# print(imparesLista(l1))
# print(imparesLista(l2))
print(compararImparesLista(l1,l2))

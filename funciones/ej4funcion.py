import random

def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def agregarNumero(lista,numero):
    while numero in lista:
        return 'el numero esta en lista'
    if numero not in lista:
        lista.append(numero)
        return lista

l1=llenarLista(10,20)
print(l1)
#num=int(input('numero: '))
print(agregarNumero(l1,15))
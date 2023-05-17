import random

def llenarLista(tam1, tam2,rango1, rango2):
    lista=[]
    lista=[random.randrange(rango1,rango2) for i in range(tam1,tam2)]
    return lista

def ordenAscendente(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    return lista 

def cuartilLista(lista):
    total=[]
    for i in range(4):
        i+=1
        cuartil=i*((len(lista)+1)/4)
        total.append(cuartil)
    return total


def quintilLista(lista):
    total=[]
    for i in range(5):
        i+=1
        quintil=i*((len(lista)+1)/5)
        total.append(quintil)
    return total
    
def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

l1=llenarLista(10,20,0,100)
print(ordenAscendente(l1))
print('cuartiles',cuartilLista(l1))
print('quintiles',quintilLista(l1))
print('promedio cuartiles',promedioLista(cuartilLista(l1)))
print('promedio quintiles',promedioLista(quintilLista(l1)))



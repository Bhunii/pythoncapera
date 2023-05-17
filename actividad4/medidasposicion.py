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
    # ordenAscendente(cuartil1)
    cuartil=1*((len(lista)+1)/4)
    total.append(cuartil)
    cuartil=2*((len(lista)+1)/4)
    total.append(cuartil)
    cuartil=3*((len(lista)+1)/4)
    total.append(cuartil)
    cuartil=4*((len(lista)+1)/4)
    total.append(cuartil)
    return total


def quintilLista(lista):
    total=[]
    quintil=1*((len(lista)+1)/5)
    total.append(quintil)
    quintil=2*((len(lista)+1)/5)
    total.append(quintil)
    quintil=3*((len(lista)+1)/5)
    total.append(quintil)
    quintil=4*((len(lista)+1)/5)
    total.append(quintil)
    quintil=5*((len(lista)+1)/5)
    total.append(quintil)
    return total
    
def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

l1=llenarLista(200,2500,100,500)
print(ordenAscendente(l1))
print('cuartiles',cuartilLista(l1))
print('quintiles',quintilLista(l1))
print('promedio cuartiles',promedioLista(cuartilLista(l1)))
print('promedio quintiles',promedioLista(quintilLista(l1)))



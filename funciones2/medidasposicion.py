import random

def llenarLista(tam1, tam2,rango1, rango2):
    lista=[]
    tam=random.randint(tam1,tam2)
    for i in range(tam):
        num=random.randrange(rango1,rango2)
        lista.append(num)
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
    for i in range(3):
        i+=1
        cuartil=round(i*((len(lista)+1)/4),3)
        total.append(cuartil)
    return total


def quintilLista(lista):
    total=[]
    for i in range(4):
        i+=1
        quintil=round(i*((len(lista)+1)/5),3)
        total.append(quintil)
    return total
    
def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def promedioIndividualCuartil(lista1, lista2):
    total=[] 
    aux1=int(lista1[0]//1)
    res1=lista2[:aux1]
    prod=promedioLista(res1)
    total.append(prod)
    aux2=int(lista1[1]//1)
    res2=lista2[aux1:aux2]
    prod1=promedioLista(res2)
    total.append(prod1)
    aux3=int(lista1[2]//1)
    res3=lista2[aux2:aux3]
    prod2=round(promedioLista(res3),3)
    total.append(prod2)
    res4=lista2[aux3:]
    prod3=round(promedioLista(res4),3)
    total.append(prod3)
    return total

def hallarX(lista1, lista2):
    total=[]
    for i in range(len(lista1)):
        aux1,aux2=0,0
        if lista1[i]%1 !=0:           
            aux1=int(lista1[i]//1)-1
            aux2=aux1+1
            #print(aux1,',',aux2)
            res=(lista2[aux1]+lista2[aux2])/2
            total.append(res)
        elif lista1[i]%1 ==0:
            res=lista1[i]//1            
            total.append(res)          
    return(total)

def cuartilListaNumero(lista,numero):
    total=[]
    while numero>4:
        numero=int(input('ingrese otro numero:'))
    cuartil=round(numero*((len(lista)+1)/4),3)
    total.append(cuartil)
    return total

def quintilListaNumero(lista,numero):
    total=[]
    while numero>5:
        numero=int(input('ingrese otro numero:'))
    cuartil=round(numero*((len(lista)+1)/5),3)
    total.append(cuartil)
    return total

#if aux3 in lista2:
    #   aux3=aux3-1
    #   res=lista2[aux3]
#else:
    #res=(f'posicion {aux3} fuera de rango')            
    #total.append(res)

l1=llenarLista((10),(20),(0),(100))
print(ordenAscendente(l1))
print('cuartiles',cuartilLista(l1))
print('quintiles',quintilLista(l1))
print('promedio cuartiles',promedioLista(cuartilLista(l1)))
print('promedio quintiles',promedioLista(quintilLista(l1)))
print('posicion x en cuartiles',hallarX((cuartilLista(l1)),(ordenAscendente(l1))))
print('posicion x en quintiles',hallarX((quintilLista(l1)),(ordenAscendente(l1))))
num=int(input('ingrese un numero de cuartil:'))
print('cuartiles',cuartilListaNumero((l1),num))
num=int(input('ingrese un numero quintil:'))
print('quintiles',quintilListaNumero((l1),num))
print('promedio 1 acurtil',promedioIndividualCuartil((cuartilLista(l1)),(ordenAscendente(l1))))
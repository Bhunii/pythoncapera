def sumaLista(lista):
    suma=0
    for x in lista:
        suma+=x
    return suma

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def menorLista(lista):
    menor = 1000000
    for i in lista:
        if i < menor:menor=i
    return menor

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

def sumaPares(lista):
    suma=0
    for i in lista:
        if i%2==0:
            suma+=i
    return suma

def ordenAscendente(lista):
    k = len(lista)
    for i in range(k):
        for j in range(i + 1, k):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

def diccionarioPuntajesTotales(lista):
    diccionario= {}
    for persona in lista:
        total_puntaje= persona.getPuntajeLectura() + persona.getPuntajeMatematicas() + persona.getPuntajeIngles() + persona.getPuntajeNaturales()
        diccionario[persona.getIdentificador()] = total_puntaje
    return diccionario


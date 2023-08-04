import random

def llenarLista(tam,rango1, rango2):
    lista = []
    for i in range(tam):
        num = random.randint(rango1, rango2)
        if num not in lista:
            lista.append(num)
    return lista


def factorialLista(lista):
    factorial = []
    for num in lista:
        fact = num
        for i in range(num-1, 1, -1):
            fact *= i
        factorial.append(fact)
    return factorial
            

l1=llenarLista(15,2,15)
print(l1)
print(factorialLista(l1))


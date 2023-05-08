import random

lista=[]
tam=random.randint(15,20)
#print(tam)
for i in range(tam):
    num=random.randrange(50)
    if num not in lista:
        lista.append(num)

n=int(input('ingresa un numero entero: '))
while n in lista:
    print('el numero esta en lista')
    n=int(input('ingresa un numero entero: '))
    
lista.append(n)
tam=tam+1

print(lista)

    

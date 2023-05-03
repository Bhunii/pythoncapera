import random
lista=[]
sum, total, prod=0, 0, 0
tam=random.randint(10,20)
print(tam)
for i in range(tam):
    num=random.randrange(100)
    lista.append(num)
print(lista)

for i in range(len(lista)):
    sum+=lista[i]
    total=sum
    prod = total//len(lista)
print(f'la suma total es de: {total}')
print(f'la promedio es de: {prod}')

mayor = 0
menor = 1000000
for i in lista:
    if i > mayor:
        mayor=i
    if i < menor:
        menor=i
print(f'el mayor es: {mayor}')
print(f'el menor es: {menor}')


'''
moda = 0
for i in lista:
    cont=
    for j in lista+1:
        if i==j:
            moda=j
print(f'la moda es: {moda}')
'''
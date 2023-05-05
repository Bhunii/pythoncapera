import random

lista=[]
lista2=[]
tam=random.randint(15,20)
#print(tam)
for i in range(tam):
    num=random.randrange(0,9)
    lista.append(num)

tam2=random.randint(15,20)
#print(tam2)
for i in range(tam2):
    num2=random.randrange(0,9)
    lista2.append(num2)

print(lista)
print(lista2)
sum1, sum2 = 0, 0
for i in lista:
    sum1+=lista[i]
    sum2+=lista2[i]
    if sum1>sum2:
        max=sum1
    if sum2>sum1:
        max=sum2

mayor1, mayor2 = 0, 0
menor1, menor2 = 1000000, 1000000
for i in lista:
    if i > mayor1:
        mayor1=i
    if i < menor1:
        menor1=i
for i in lista2:
    if i > mayor2:
        mayor2=i
    if i < menor2:
        menor2=i
if mayor1 > mayor2:
    maxmayor=mayor1
else:
    maxmayor=mayor2
if menor1 > menor2:
    minmenor=menor1
else:
    minmenor=menor2
sumtotal=sum1 + sum2
tamtotal=tam + tam2
prod=sumtotal/tamtotal
print(sumtotal, tamtotal)
print(sum1, sum2)#su de cada lista
print(max)#es la suma mayor
print(maxmayor)#mayor ambas listas
print(minmenor)#menor ambas listas
print(prod)#prod de las sumas de las dos listas
#print(lista2)


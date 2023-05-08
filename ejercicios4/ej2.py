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

#print(lista)
#print(lista2)  
print(sumtotal, tamtotal)
print(sum1, sum2)#su de cada lista
print(max)#es la suma mayor
print(maxmayor)#mayor ambas listas
print(minmenor)#menor ambas listas
print(prod)#prod de las sumas de las dos listas
#print(par1, impar1)
#print(par2, impar2)

prod1=sum1/tam
prod2=sum2/tam2
if prod1 > prod:
    print(f'el promedio {prod1} de la lsita1 esta por encima del conjunto')
else:
    print(f'el promedio {prod1} de la lsita1 esta por debajo del conjunto')

if prod2 > prod:
    print(f'el promedio {prod2} de la lsita2 esta por encima del conjunto')
else:
    print(f'el promedio {prod2} de la lsita2 esta por debajo del conjunto')


par1, par2 = [], []
impar1, impar2 = [], []
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        par1.append(lista[i])
    else:
        impar1.append(lista[i])

for i in range(len(lista2)):
    if lista2[i] % 2 == 0:
        par2.append(lista2[i])
    else:
        impar2.append(lista2[i])

if len(par1) > len(par2):
    print(f'la lista1 tiene mayor cantidad de pares ({len(par1)}) ')  
elif len(par1) < len(par2):
    print(f'la lista2 tiene mayor cantidad de pares ({len(par2)}) ') 
else:
    aux1=len(par1)
    aux2=len(par2)
    if aux1 ==  aux2:
        print('ambos tienen la misma cantida de pares')

if len(impar1) > len(impar2):
    print(f'la lista1 tiene mayor cantidad de impares ({len(impar1)}) ')       
elif len(impar1) < len(impar2):
    print(f'la lista2 tiene mayor cantidad de impares ({len(impar2)}) ')
else:
    aux3=len(impar1)
    aux4=len(impar2)
    if aux3 ==  aux4:
        print('ambos tienen la misma cantida de impares')






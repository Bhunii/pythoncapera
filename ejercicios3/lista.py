import random

lista=[]
sum, total, prod=0, 0, 0
tam=random.randint(10,20)
print(tam)
for i in range(tam):
    num=random.randrange(100)
    lista.append(num)
print(lista)

#suma total y promedio
for i in range(len(lista)):
    sum+=lista[i]
    total=sum
    prod = total//len(lista)
print(f'la suma total es de: {total}')
print(f'la promedio es de: {prod}')

#mayor y menor
mayor = 0
menor = 1000000
for i in lista:
    if i > mayor:
        mayor=i
    if i < menor:
        menor=i
print(f'el mayor es: {mayor}')
print(f'el menor es: {menor}')

#moda
k=len(lista)
cant=0
for i in range(k):
    cont=0
    for j in range(k):
        if lista[i] == lista [j]:
            cont= cont+1
    if cont>cant:
        cant = cont 
        moda = lista[i]
if cant == 1:
    print('no hay moda')
else:
    print(f'la moda es {moda} se repite {cant}')

#mediana
m=lista
#m.sort()
for i in range(tam):
    for j in range(i+1,tam):
        if m[i]>m[j]:
            aux=m[i]
            m[i]=m[j]
            m[j]=aux
if tam%2 == 0:
    y = (tam // 2) 
    j = y-1
    med = (m[y] + m[j]) / 2
    #print(m)
    #print(m[y])
    #print(m[j])
    print(f'la mediana es {med}')
if tam%2 != 0:
    div=tam//2
    #v=div-1
    #print(m)
    #print (div)
    print(f'la mediana es {m[div]}')

#desviacion estandar
resta = []
sum2, total2 = 0, 0
for i in lista:
    r=i - prod
    resta.append(r)
for i in range(len(resta)):
    resta[i]=resta[i]**2
for i in range(len(resta)):
    sum2+=resta[i]
    total2=sum2
total3=sum2//tam
    #print(total3)
r=total3
x=0
while x * x <= total3:
    x+=0.0001
print(f'la desviacion estandar es {x:.3f}')

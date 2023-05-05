#15 a 20
# entre 0 y 9
#si esta
#si esta cuanta veces 
#la posicion
import random

lista=[]
tam=random.randint(15,20)
#print(tam)
for i in range(tam):
    num=random.randrange(0,9)
    lista.append(num)
#print(lista)


num=int(input('ingrese numero: '))
while num not in lista:
    print('no esta en lista')
    num=int(input('ingrese otro numero: '))


for i in range(tam):
    if num == lista[i]:
        break
print('si esta')
print(lista)
print(tam)

for c in lista:
    cont=0
    for a in lista:
        if num == a:
            cont+=1
if cont==1:
    print(f'{num} no se repite')
else:
    print(f'{num} se repite {cont}')

rep=[]
for i in range(len(lista)):
        if num == lista[i]:
            rep.append(i)

print(f'El numero {num} esta en la posicion {rep}')


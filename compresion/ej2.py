import random

tam=random.randint(20,30)
lista=[round(random.random()*5,2) for i in range(tam)]

aprobo=[x for x in lista if x >= 3 ]
reprobo=[x for x in lista if x<3]

uno=[x for x in lista if x>0 and x<1]
dos=[x for x in lista if x>=1 and x<2]
tres=[x for x in lista if x>=2 and x<3]
cuatro=[x for x in lista if x>=3 and x<4]
cinco=[x for x in lista if x>=4 and x<=5]

suma, suma2=0, 0
for i in range(len(aprobo)):
    suma+=aprobo[i]
prod=round(suma/len(aprobo),2)
for i in range(len(reprobo)):
    suma2+=reprobo[i]
prod2=round(suma2/len(reprobo),2)


print(lista)
print(aprobo)
print(reprobo)
print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)
print(prod)
print(prod2)
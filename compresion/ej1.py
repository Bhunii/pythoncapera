import random
import math

tam=random.randint(5,10)
lista=[random.randrange(100) for i in range(tam)]

elevado=[math.sqrt(k) if k%2==0 else k**2 for k in lista]
print(lista)
print(elevado)


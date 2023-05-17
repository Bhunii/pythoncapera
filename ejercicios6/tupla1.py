import random 

tam=random.randint(0,15)
t=()
for i in range(tam):
    num=random.randrange(100)
    t+=(num,)

print(t)

aux1=len(t)//2
t2=t[0:aux1]
t3=t[aux1:]
print(t2)
print(t3)


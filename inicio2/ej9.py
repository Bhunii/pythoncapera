x=int(input('numero: '))
n=int(input('numero al que lo eleva: '))
res=1

for k in range(n):
    res= res * x

print(f'{x} elevado a {n} da {res}')
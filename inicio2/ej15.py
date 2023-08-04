n = int(input("Introduce un un valor no negativo: "))
for i in range(n,0, -1):
    for j in range(i):
        print(1+j,end=" ")
        j=j-1
    print("")
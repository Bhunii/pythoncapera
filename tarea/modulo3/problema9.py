a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

if a >= b and a >= c:
    print(f"{a} es el número mayor")
elif b >= a and b >= c:
    print(f"{b} es el número mayor")
else:
    print(f"{c} es el número mayor")
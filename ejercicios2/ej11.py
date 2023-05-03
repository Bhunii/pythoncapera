n1 = int(input("Ingresa un número entero: "))
n2 = int(input("Ingresa otro número entero: "))

mayor = max(n1, n2)
menor = min(n1, n2)

cociente = 0
residuo = 0
while mayor >= menor:
    mayor -= menor
    cociente += 1
residuo = mayor

print(f"El cociente de dividir el mayor entre el menor es: {cociente}")
print(f"El residuo de dividir el mayor entre el menor es: {residuo}")



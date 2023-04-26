# num=1
# print(type(num))
# num="sena"
# print(type(num))
num=1 #se define la variable 'num' con un valor de 1
cont=0 #se define la variable 'cont' con un valor de 0
sum=0 #se define la variable 'sum' con un valor de 0
menor=1000000 #se define la variable 'menor' con un valor de 1000000
mayor=0 #se define la variable 'mayor' con un valor de 0
while num!=0: #se inicia un ciclo while en donde la variable 'num' tiene que ser diferente de 0 
    num=int(input('ingrese numero')) #'num' es igual a una entrada de dato tipo entero
    cont=cont+1 #'con' es un contador ue es igual a la misma varible mas una constante
    sum=sum+num #'sum' realiza la suma de todos los numeros en donde cada vez que un numero ingrese se sume a 'sum'
    if num>mayor: #si 'num' es mayor que 'mayor' 
        mayor=num #guardar el numero mayor
    if num<menor and num!=0: #si 'num' es menor que 'menor' y tambien que 'num' no sea igual a 0 para evitar que lo cuente como menor
        menor=num #la variable de alguna forma se guarda
print(f'fueron ingresados {cont-1} numeros')#se imprime el 'cont-1' para evitar que cuente el cero
print(f'La suma es {sum}')#se imprime la sumatoria total de todos los numoeros ingresados
print(f'El promedio es {sum/(cont-1)}')#se imprime promedio donde se divide 'sum' por 'cont-1'
print(f'El mayor es {mayor}')#se imprime variable 'mayor'
print(f'El menor es {menor}')#se impime variable 'menor'
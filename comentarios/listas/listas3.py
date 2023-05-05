import random #se importa la libreria random para la aleatoriedad
lista=[] 
cuadrado=[]
tam=random.randint(5,10) #en 'tam' se llama a random y .randint genera un numero tipo entero entre a(5) y b(10)
print(tam) 
for i in range(tam): #se crea ciclo for con un tamaño del numero generado 
    num=random.randrange(100) #en 'num' se llama a random y .randrange genera un numero entre '0'(cuando no se define desde donde empieza se toma como 0)
    #hasta '100' 
    lista.append(num) #se genere un numero que sera agregado el doto despues de la ultimo dato en la lista
print(lista)

for i in range(len(lista)): #ciclo for el tamaño de lista
    cuadrado.append(lista[i]**2) #cuando lista en esta en la posicion i en '1' que seria cero toma ese dato y es elevado por dos despues lo agrega a cuadrado
    #lista[i]=lista[i]**2
    # print(lista[i]*lista[i])
    # print(lista[i]**2)
    # print(math.pow(lista[i],2))

print(cuadrado) #imprime la lista 'cuadrado' con los datos elevados 
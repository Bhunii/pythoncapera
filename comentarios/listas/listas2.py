lista=[] #se crea lista vacia
lista.append(100) #el .append agrega al doto despues de la ultimo dato en este caso como esta vacia '100' seria el primer dato
lista.append(50) #'50' el segundo y asi sucesivamente
lista.append(-100)
lista.append(20)
lista.append(5)

print(lista)
lista.insert(-2,'prueba') #el .insert agrega un dato pero se elige la posicion agregandose uno mas arriba quedando en la posicion de '-3' entre  '20' y '-100'
print(lista)
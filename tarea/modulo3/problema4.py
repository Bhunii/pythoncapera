# Ordenar canciones alfabeticamente (el .sort cumple esa funcionalidad )
# y el str el numero para a string

canciones = []

num_canciones = int(input("Ingrese la cantidad de canciones que desea agregar: "))

for i in range(num_canciones):
    cancion = input("Ingrese el título de la canción #" + str(i+1) + ": ")
    canciones.append(cancion)

canciones.sort()
print("Estas son las canciones en orden alfabético:")
for cancion in canciones:
    print(cancion)
    
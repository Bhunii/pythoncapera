import csv

titulo = input("Ingresa el título de la película: ")
genero1 = input("Ingresa el primer género: ")
genero2 = input("Ingresa el segundo género: ")
genero3 = input("Ingresa el tercer género: ")

nueva_pelicula = {titulo,genero1,genero2,genero3}

with open('archivosCSV/peliculas.csv', 'a', newline='') as file:
    escribir=csv.writer(file)
    escribir.writerow(nueva_pelicula)

print('La pelicula ha sido agregada')

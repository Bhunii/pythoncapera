import csv

with open('archivosCSV/canciones.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print('1er Apellido: {0}, 2do Apellido: {1}, 1er Nombre: {2}, Cancion Favorita: {3}'.format(row[0],row[1],row[2],row[3]))
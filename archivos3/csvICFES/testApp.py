from Persona import *

import csv
personas=[]
with open('archivos3/csvICFES/personas_icfes.csv', encoding='utf-8') as icfesFile:
    csvReader=csv.reader(icfesFile)
    for row in csvReader:
        objeto=Persona(row[0],row[1],row[2],row[3],row[4],row[5])
        #print(objeto.verDatos())
        personas.append(objeto)

for ap in personas:
    print(ap.getGenero())
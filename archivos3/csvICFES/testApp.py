from Persona import *
from funciones.allfunciones import *

import csv
personas=[]
with open('archivos3/csvICFES/personas_icfes.csv', encoding='utf-8') as icfesFile:
    csvReader=csv.reader(icfesFile)
    for row in csvReader:
        objeto=Persona(row[0],row[1],row[2],row[3],row[4],row[5])
        #print(objeto.verDatos())
        personas.append(objeto)

lsGerne=[]
for ap in personas:
    lsGerne.append(ap.getGenero())

puntajes_lectura = [people.getPuntajeLectura() for people in personas]
promedio_lectura = promedioLista(puntajes_lectura)
#print('promedio lectura:',promedio_lectura)
#print(abajoArriba(puntajes_lectura))

puntajes_matematicas = [people.getPuntajeMatematicas() for people in personas]
menor_matematicas = menorLista(puntajes_lectura)
#print('menor puntaje matematicas:',menor_matematicas)

puntajes_ingles = [people.getPuntajeIngles() for people in personas]
#print('Suma numeros pares puntaje ingles:', sumaPares(puntajes_ingles))

puntajes_naturales = [people.getPuntajeNaturales() for people in personas]
#print('orden ascendente puntaje naturales:', ordenAscendente(puntajes_naturales))

diccionario_definitivo = diccionarioPuntajesTotales(personas)
#print(diccionario_definitivo)
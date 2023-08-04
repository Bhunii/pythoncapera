#codigo de departamento = representaria a documento
#'archivos3/Resultados_Saber_11_2018-1_Refinado.csv'
import csv
lista=[]
with open('archivos3/csvICFES/Resultados_Saber_11_2018-1_Refinado.csv', encoding='utf-8') as csvDataFile:
    csvReader=csv.reader(csvDataFile)
    next(csvReader)
    for row in csvReader:
        #print(row)
        estudiante=row[5]
        genero=row[2]
        puntaje_lectura=row[67]
        puntaje_matematicas=row[70]
        puntaje_naturales=row[73]
        puntaje_ingles=row[79]
    
        lista.append((estudiante, genero, puntaje_lectura, puntaje_matematicas, puntaje_naturales, puntaje_ingles))

with open('archivos3/csvICFES/personas_icfes.csv', 'w', encoding='utf-8') as file_icfes:
    for i in lista:
        file_icfes.write(','.join(str(item) for item in i) + '\n')
     
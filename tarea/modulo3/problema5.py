# Promedio Altura Por Genero
# Se crean listas para almacenar los datos ingresados, el append permite identificar la lista,
# el sum suma todo los datos y el round redondea a dos decimales

alturas_chicos = []
alturas_chicas = []

cant_chicos = int(input("Ingrese la cantidad de chicos en la clase: "))
cant_chicas = int(input("Ingrese la cantidad de chicas en la clase: "))

for i in range(cant_chicos):
    altura_chico = float(input("Ingrese la altura del chico #" + str(i+1) + ": "))
    alturas_chicos.append(altura_chico)

for i in range(cant_chicas):
    altura_chica = float(input("Ingrese la altura de la chica #" + str(i+1) + ": "))
    alturas_chicas.append(altura_chica)

promedio_chicos = sum(alturas_chicos) / cant_chicos
print("El promedio de altura de los chicos es:", round(promedio_chicos, 2), "m")

promedio_chicas = sum(alturas_chicas) / cant_chicas
print("El promedio de altura de las chicas es:", round(promedio_chicas, 2), "m")


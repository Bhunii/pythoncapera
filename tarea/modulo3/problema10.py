# Cuestionario de anime
# el lower convierte la cadena en minusculas


puntaje = 0

# Pregunta 1
respuesta1 = input("1. El anime Naruto fue creado por Masashi Kishimoto. (V/F) ")
if respuesta1.lower() == "v":
    print("¡Correcto!")
    puntaje += 1
else:
    print("Incorrecto. La respuesta correcta es verdadero.")

# Pregunta 2
respuesta2 = input("2. En Dragon Ball Z el personaje que mas muerio fue Krillin. (V/F) ")
if respuesta2.lower() == "v":
    print("¡Correcto!")
    puntaje += 1
else:
    print("Incorrecto. La respuesta correcta es falso.")

# Pregunta 3
respuesta3 = input("3. El personaje principal de One Piece es Monkey D. Luffy. (V/F) ")
if respuesta3.lower() == "v":
    print("¡Correcto!")
    puntaje += 1
else:
    print("Incorrecto. La respuesta correcta es verdadero.")

# Pregunta 4
respuesta4 = input("4.  En el anime Re:Zero nunca se menciona a la bruja de los celos. (V/F) ")
if respuesta4.lower() == "f":
    print("¡Correcto!")
    puntaje += 1
else:
    print("Incorrecto. La respuesta correcta es verdadero.")

# Pregunta 5
respuesta5 = input("5. La historia de Attack on Titan se centra en la humanidad que vive dentro de tres enormes muros para protegerse de los titanes. (V/F) ")
if respuesta5.lower() == "v":
    print("¡Correcto!")
    puntaje += 1
else:
    print("Incorrecto. La respuesta correcta es verdadero.")

# Pregunta 6
respuesta6 = input("5. Marin es una chica que no le gusta hacer cosplay. (V/F) ")
if respuesta6.lower() == "f":
    print("¡Correcto!")
    puntaje += 1
else:
    print("Incorrecto. La respuesta correcta es verdadero.")

# Mostrar puntaje final
print("Tu puntaje final es de " + str(puntaje) + " puntos.")

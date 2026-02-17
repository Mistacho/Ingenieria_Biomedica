import random
"""
Autor: David Aznar Tornero
Versión: 1.0.0
Fecha: 2026-02-17

Haz un programa que te adivine el número que has pensado entre 1 y 100. Cada vez que el programa te diga una
número le tienes que contestar si es mayor o menor que el que has pensado
"""

#Importando la libreria random podemos generar un numero aleatorio del 1 al 100
numero = random.randint(1,100)
nBajo = 1
nAlto = 100
#Con esta variable nos evitamos usar break dentro del bucle y así no complicamos la lógica del programa
acertado = False

while (nBajo != nAlto and not acertado):
    respuesta = input(f"El número que estabas pensando es el {numero} ? (mayor o mayomenor)")
    if (respuesta == "mayor"):
        nAlto = numero
        numero = random.randint(nBajo,nAlto)
    elif (respuesta == "menor"):
        nBajo = numero
        numero = random.randint(nBajo,nAlto)
    elif (respuesta == "si"):
        acertado = True

print(f"Tu numero pensado es el {numero} !!!")
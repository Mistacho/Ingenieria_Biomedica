"""
Autor: David Aznar Tornero
Versión: 1.0.0
Fecha: 2026-02-09
"""

'''
----------------------------- TIPOS DE BUCLES -----------------------------------------------------------------
while (COND)  -->  BUCLE CONTROLADO POR CONDICIÓN
    Acciones deben causar cambio en los valores de las variables que intervienen en la condición (para que en 
    algún momento se salga del bucle)

while TRUE:  -->  BUCLE INFINITO
    Acción: se rompe con break o cuando aborto el programa

for variable in iterable/ variable in range (num)  -->  BUCLE CONTROLADO POR CANTIDAD
    Acciones con elementos de variable iterable
---------------------------------------------------------------------------------------------------------------
'''

#Que imprimen los siguientes programas
#Apartado a)
i = 3
while i < 10:
    i += 2
    print(i)
print("Hecho")
#Imprime 5,7,9,11, Hecho

#Apartado b)
i = 1
while i < 100:
    i *= 2
    print(i)
#Imprime 2,4,8,16,32,64,128

#Apartado c)
i = 10
while i < 2:
    i *= 2
    print(i)
#Nada

#Apartado d)
i = 0
while i <= 3:
    print(i)
    i += 1
print("Hecho")
#Imprime 0,1,2,3,Hecho

#Apartado e)
'''
i = 0
while i < 10:
    print(i)
#Imprime 0,0,0,0,0.... INFINITO

'''

'''
----------------------------- OPERADOR BREAK -----------------------------------------------------------------
while True:
    linea=input(“Introduce tu deseo (fin para terminar)”)
    if (linea=="fin"):
        break  -->  Lo que hace es salirse del bucle sin ejecutar 
    print(“Deseas ”,linea)
print ("Terminado")
---------------------------------------------------------------------------------------------------------------

----------------------------- OPERADOR CONTINUE -----------------------------------------------------------------
while(True):
    linea=input(">")
    if (linea[0]=="#"):
        continue  -->  Lo que hace es volver al inicio del while sin ejecutar lo de debajo
    if (linea=="fin"):
        break
    print(linea)
print("¡Terminado!")
---------------------------------------------------------------------------------------------------------------
'''
"""
Autor: David Aznar Tornero
Versión: 1.0.0
Fecha: 2026-02-16
"""

#Declaramos las variables del problema
err1 = 1
err2 = 1
errTot = 1
resultado = 0

#Solicitamos los numeros al usuario
n1 = int(input("Introduzca el primer numero "))
while n1 < 0 and err1 < 3:
    n1 = int(input("Vuelva a introducir el primer numero, debe ser positivo "))
    err1 += 1
    errTot += 1

if(n1 > 0):
    n2 = int(input("Introduzca el segundo numero "))
    
    while (n2 < n1) and (err2 < 3) and (errTot < 4):
        n2 = int(input("Vuelva a introducir el segundo numero, debe ser mayor que el primero "))
        err2 += 1
        errTot += 1
    
    if(n2 > n1):
        for a in range (n1 + 1,n2):
            resultado = resultado + a
        print (resultado)
    else:
        print("Lo siento, ha agotado los intentos posibles")
else:
    print("Lo siento, ha agotado los intentos posibles")

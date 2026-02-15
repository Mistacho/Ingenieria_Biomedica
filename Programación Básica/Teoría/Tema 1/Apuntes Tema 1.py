"""
Autor: David Aznar Tornero
Versión: 1.0.0
Fecha: 2026-02-08
"""

'''
ERRORES DE SINTAXIS: los más fáciles de corregir. Si violas la ‘gramática’ de Python, éste te avisa.

ERRORES DE EJECUCIÓN: se producen mientras el programa se está ejecutando (run, correr); cuando
alcanza la línea con el error, el programa termina de manera anómala (crash) con un mensaje y un rastreo
de dónde se ha producido el error (traceback)

ERRORES SEMÁNTICOS: los más difíciles: el programa no termina de manera anómala pero aún así no hace 
lo que querías que hiciera.
'''

'''
#Error sintáctico (Faltan los : al final del if)

a = input("Dime un numero entre 0 y 10")
if(int(a) < 5)
    print("Hola")

#Error sintáctico (print mal escrito)
a = input("Dime un numero entre 0 y 10")
if(int(a) < 5):
    printt("Hola")

#Error semántico (Nunca escribirá Hola)
a = input("Dime un numero entre 0 y 10")
if(int(a) > 15):
    print("Hola")

'''

"""
--------------------------------- TIPOS DE VALORES -------------------------------------------
    Valores enteros (INT)  -->  int() 
    Valores decimales (FLOAT)  -->  float()
    Cadenas de caracteres (STRING)  -->  str()
    Valores booleanos (BOOLEAN)  -->  bool()
----------------------------------------------------------------------------------------------
    Python declara las variables de forma dinámica, eso quiere decir que las variables
    serán del tipo que sea el contenido de dentro. De esta forma, podremos tener variables
    que durante un momento del código sean por ejemplo enteros y después si nos interesa
    cadenas de caracteres y python no se quejará
----------------------------------------------------------------------------------------------


--------------------------------------- OPERADORES -------------------------------------------
    El operador  +  -->  Suma
    El operador  -  -->  Resta
    El operador  *  -->  Multiplicación
    El operador  /  -->  División float
    El operador  //  -->  División entera
    El operador  **  -->  Elevado
    El operador  %  -->  Resto

---------------------------------- OPERADORES CON CADENAS ------------------------------------
    3 * 'a'  -->  aaa
    'hola' + 'cris'  -->  holacris

"""








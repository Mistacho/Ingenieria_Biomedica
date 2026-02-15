#Establecemos la edad
EDAD = 21

#Solicitamos la edad de dos personas más
ed1 = int(input("Introduzca la primera edad: "))
ed2 = int(input("Introduzca la segunda edad: "))

#Asusmimos que partimos de ser el mayor
orden = 1

if(EDAD > ed1) and (EDAD > ed2):
    print("Eres el mayor de los tres")
elif(EDAD < ed1) and (EDAD < ed2):
    print("Eres el pequeño de los tres")
    orden = orden + 2
else:
    print("Eres el mediano de los tres")
    orden = orden + 1

print("El orden es" , orden)
#Primero solicitaremos ambas notas
teoria = int(input("Introduzca la nota de teoría: "))
practica = int(input("Introduzca la nota de prácticas: "))

#Establecemos la condicion para que se tenga que superar un 4 en ambas partes
if(teoria >= 4) and (practica >= 4):
    notaFinal = (teoria + practica)/ 2

else:
    notaFinal = 0

print("La nota final obtenida es:" , notaFinal)
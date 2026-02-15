#Primero solicitaremos ambas notas
teoria = int(input("Introduzca la nota de teoría: "))
practica = int(input("Introduzca la nota de prácticas: "))

#Establecemos la condicion para que se tenga que superar un 4 en ambas partes
if(teoria >= 4) and (practica >= 4):
    notaFinal = (teoria + practica)/ 2

else:
    notaFinal = 0

#Dependiendo de la nota final imprimiremos por pantalla la opción correcta relacionada
if(notaFinal < 5):
    print("SUSPENSO")
elif(5 < notaFinal < 7):
    print("APROBADO")
elif(7 < notaFinal < 9):
    print("NOTABLE")
else:
    print("SOBRESALIENTE")

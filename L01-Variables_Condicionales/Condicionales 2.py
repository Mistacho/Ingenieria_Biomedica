#Primero declaramos la variable de mi altura
MIALTURA = 170

#Solicitamos al usuario su altura
altura = int(input("Introduzca su altura "))

#Creamos el condicional para ver si es más alto que yo, más bajo, o de la misma estatura
if(MIALTURA > altura):
    print("Es usted más bajo que yo")
elif(MIALTURA < altura):
    print("No puede ser, soy más bajo que usted")
else:
    print("Vaya, somos de la misma estatura")
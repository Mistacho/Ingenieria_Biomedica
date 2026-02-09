'''
1) Entrada de datos

El programa debe pedir:
    Nombre del usuario.
    Edad (en años).
    Es estudiante (Si/No).
    Día de la semana (Lunes, Martes, …, Domingo).
    Saldo disponible (en euros).

2) Validación (muy importante)

Usa .isdigit() para asegurarte de que edad y saldo son números enteros.

Si alguno no es numérico, mostrar:
"Error: edad y saldo deben ser números." y terminar.

3) Reglas de acceso

    Edad mínima para entrar: 16 años.
    Precio base de entrada: 6€.
    Si el usuario es estudiante y el día es Sábado o Domingo, el precio es 4€ (descuento).

4) Salida (mensajes)

Si tiene menos de 16 años:
"Lo siento [Nombre], debes tener al menos 16 años para entrar."

Si cumple edad pero no tiene saldo suficiente:
"Saldo insuficiente. Necesitas [Precio]€ y tienes [Saldo]€."

Si cumple todo: restar el precio y mostrar:
"Acceso permitido. Bienvenido/a, [Nombre]. Saldo restante: [SaldoRestante]€."

'''

"""
Autor: David Aznar Tornero
Versión: 1.0.0
Fecha: 2026-02-09
"""

#Declaramos todas las preguntas que hay que hacerle al usuario
nombre = input("Introduzca su nombre")
edad = int(input("Introduzca su edad"))
estudiante = input("Eres estudiante (Si/No)")
dia_semana = input("Introduzca el dia de la semana")
saldo = float(input("Introduzca el saldo (euros)"))
precio = 6.0


if(edad >= 16):
    if(estudiante == "Si" and (dia_semana == "Sabado" or dia_semana == "Domingo")):
        precio = 4.0

    if(saldo > precio):
        saldo_restante = saldo - precio
        print("Acceso permitido. Bienvenido/a, " + nombre + ". Saldo restante: " + saldo_restante + " €.")
    else:
        print("Saldo insuficiente. Necesitas " + precio + " € y tienes " + saldo + " €.")

else:
    print("Lo siento, " + nombre +  " no eres mayor de 16 años")


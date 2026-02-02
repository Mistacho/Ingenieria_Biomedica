''' 
El programa debe:
1. Entrada de usuario: Solicitar al usuario que introduzca la frecuencia cardíaca en latidos por minuto (bpm). Asegúrate de que el programa indique claramente la unidad en la que se debe introducir la frecuencia cardíaca
2. Definir rangos normales:
    ◦ Frecuencia cardíaca normal en reposo: entre 60 y 100 bpm (aproximadamente).
    ◦ Usar variables para almacenar estos límites. 
    ◦ Considerar que los límites podrían variar según el paciente, por ejemplo, usar constantes en mayúsculas para indicar los límites generales, pero usar variables para los límites específicos de un paciente. 
3. Evaluar el ritmo cardíaco:
    ◦ Utilizar sentencias condicionales (if, elif, else) para determinar si el ritmo cardíaco es normal, demasiado lento (bradicardia) o demasiado rápido (taquicardia). 
    ◦ Imprimir mensajes claros y concisos indicando la condición del ritmo cardíaco. 
        ▪ "Ritmo cardíaco normal."
        ▪ "Bradicardia: Ritmo cardíaco demasiado lento."
        ▪ "Taquicardia: Ritmo cardíaco demasiado rápido."
    ◦ Considerar el uso de operadores booleanos para definir las condiciones:  and, or, not. 
4. Añadir una alerta adicional:
    ◦ Si la frecuencia cardíaca es inferior a 40 bpm o superior a 180 bpm, el programa debe emitir una alerta de emergencia. Esto se puede hacer con una sentencia condicional anidada.
    ◦ Imprimir el mensaje: "¡¡ALERTA DE EMERGENCIA!! Ritmo cardíaco crítico."
5. Manejo de Errores:
    ◦ Considerar la posibilidad de que el usuario introduzca un valor no válido (por ejemplo, una cadena de texto en lugar de un número). Utilizar conversión de tipos (int() o float()) y manejar los posibles errores de ejecución. 
6. Comentarios:
    ◦ Asegurarse de que el código está correctamente comentado, incluyendo el autor y el propósito del programa, las unidades de la frecuencia cardiaca y el significado de las variables y las sentencias condicionales. Utilizar ambos tipos de comentarios: de una línea y de varias líneas.
7. Mejoras adicionales (opcional):
    ◦ Implementar un bucle while para que el programa pueda monitorizar continuamente el ritmo cardíaco, hasta que el usuario decida detenerlo.
    ◦ Usar un operador condicional ternario para simplificar alguna de las sentencias condicionales. 
    ◦ Los ritmos cardiacos considerados 'normales' pueden variar según la edad del paciente. Investiga este tema y modifica el programa para que tenga en cuenta la edad a la hora de evaluar el ritmo cardíaco
'''

freq = int(input("Introduzca la frecuncia caridiaca en latidos por minuto (bpm)"))
FREQMIN = 60
FREQMAX = 100

if(freq < 60):
    print("Bradicardia: Ritmo cardíaco demasiado lento.")
    if(freq < 40):
        print("¡¡ALERTA DE EMERGENCIA!! Ritmo cardíaco crítico.")
elif(freq > 100):
    print("Taquicardia: Ritmo cardíaco demasiado rápido.")
    if(freq > 180):
        print("¡¡ALERTA DE EMERGENCIA!! Ritmo cardíaco crítico.")
else:
    print("Ritmo cardíaco normal.")







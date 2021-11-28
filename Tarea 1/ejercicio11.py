"""
EJERCICIO 11.-Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es 
un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
"""
print("Saber si un año es Bisiesto")

anio = int(input("Introduzca el año: "))

if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")

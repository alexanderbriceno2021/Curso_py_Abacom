"""
EJERCICIO 5.-Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos 
corresponde.
"""
minutos = int(input("Minutos:"))
print("Horas:%d - Minutos:%d" % (minutos/60, minutos % 60))

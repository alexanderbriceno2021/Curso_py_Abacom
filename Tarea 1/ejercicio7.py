"""
EJERCICIO 7.- Realiza un programa que pida dos números ‘a’ y ‘b’ e indique si su suma es 
positiva, negativa o cero.
"""

a = int(input("Escribe el primer numero: "))
b = int(input("Escribe el segundo numero: "))

if a+b > 0:
    print("La suma es positiva")

elif a+b < 0:
    print("La suma es negativa")
else:
    print(" La suma es 0 ")

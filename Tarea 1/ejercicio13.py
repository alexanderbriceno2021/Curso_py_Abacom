"""
EJERCICIO 13.- Pedir un número por teclado y mostrar la tabla de multiplicar
"""

print("Tabala de Multiplicar")

numero = int(input("Introduzca un numero: "))

for i in range(1, 11):
    print(f"{i} x {numero} = {i*numero}")

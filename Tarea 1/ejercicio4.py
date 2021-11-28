"""
EJERCICIO 4.- Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces,
 con espacios intermedios.
"""

# Forma simple
print("Forma simple de resolver")

palabra = input("Escriba una palabra: ")
print((palabra + " ")*1000)


# Con una Función
print("Solucion con una función")

escribe_palabra = input("Escriba una palabra para repetir: ")


def repetir():
    print((escribe_palabra + " ")*1000)


repetir()

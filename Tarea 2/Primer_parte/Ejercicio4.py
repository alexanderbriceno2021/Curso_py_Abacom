"""
 
 Realiza un programa que pida al usuario cuantos números quiere introducir. 
 Luego lee todos los números y realiza una media aritmética:

"""

suma = 0
numeros = int(input("Escriba cuantos numeros quiere introducir: "))

for n in range(numeros):
    suma += float(input("Coloque el un numero: "))

print("Se an introducido", numeros, "numeros, que dan un total de ",
      suma, "y su media arimetica es", suma/numeros)

"""
EJERCICIO 3.- Dados dos números, mostrar la suma, resta, división y multiplicación de ambos
"""

# Saolición de Forma simple
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el primer numero: "))

print("La suma es: ", num1 + num2)
print("La Resta es: ", num1 - num2)
print("La Multiplicacion es: ", num1 * num2)
print("La Division es: ", num1 / num2)

# solucion con funciones
print("Operaciones Matematicas")

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

# suma


def suma():
    print("La suma es ", num1 + num2)


suma()

# Resta


def resta():
    print("La Ressta es ", num1 - num2)


resta()

# Multiplicación


def multiplicacion():
    print("La Multiplicación es ", num1 * num2)


multiplicacion()

# Division


def division():
    print("La División es ", num1 / num2)


division()

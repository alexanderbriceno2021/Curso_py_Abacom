"""
Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:

Sugerencia: Puedes utilizar la funciones sum() y range() para hacerlo más fácil.
El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo

"""

# Solucion 1 simple
suma = sum(range(0, 101, 2))
print(suma)


# solucion 2 "for"
suma = 0

num1 = int(input('Numero inicial:'))
num2 = int(input('Numero final:'))

for i in range(num1, num2+1):

    if i % 2 == 0:

        suma += i

print('\nLa suma es : ', suma)

# solucion 3 "función"


def suma_pares():
    suma = sum(range(0, 100, 2))
    print(suma)


print("\nLa suma es: ")
suma_pares()

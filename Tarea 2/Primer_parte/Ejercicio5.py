"""
5) Realiza un programa que pida al usuario un número entero del 0 al 9, 
y que mientras el número no sea correcto se repita el proceso. 
Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:


"""

lista = [1, 3, 6, 9]

while True:
    nuemero = int(input("Escriba un numero: "))

    if nuemero >= 0 and nuemero <= 9:
        break

if nuemero in lista:
    print("El numermo", nuemero, "si esta en la lista", lista)
else:
    print("El numermo", nuemero, "no esta en la lista", lista)

"""
EJERCICIO 12.- Programa que lea un carácter por teclado y compruebe si es una letra mayúscula.
"""
# solucion con una condicional

letra = input("Introduzca una letra: ")

if letra >= "A" and letra <= "Z":
    print("La letra es Mayuscula")
else:
    print("La letra es minusculas")


# Solucion con una funcion y un condicional

letra = input("Introduzca una letra: ")


def comprueba():
    if letra >= "A" and letra <= "Z":
        print("La letra es Mayuscula")
    else:
        print("Es minuscula")


comprueba()

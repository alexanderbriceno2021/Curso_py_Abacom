"""
2) Realiza un programa que lea un número impar por teclado.
Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

"""
numero = int(input("Coloque un numero: "))


while numero % 2 == 0:
    print("el numero es par")
    numero = int(input("Coloque un numero Nuevamente: "))

else:
    print("correcto el numero es impar")

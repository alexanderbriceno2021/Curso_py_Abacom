"""
1) Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de no introducir una opción válida, el programa informará de que no es correcta.

"""

print("Operaciones con dos Numeros.\n")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

while True:

    print("\n", "Que Operacion quieres realizar", "\n")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) salir")

    operacion = int(input("Elige un numero de 1 al 4: "))

    if operacion == 1:
        print(" La suma de ", num1, "+", num2, "=", num1+num2)

    elif operacion == 2:
        print("La resta de", num1, "-", num2, "=", num1-num2)

    elif operacion == 3:
        print("La multiplicación de", num1, "*", num2, "=", num1*num2)

    elif operacion > 4:
        print("\nOperacion no es correcta...!!!!!")

    else:
        break

"""
Vamos a mejorar el ejercicio anterior haciendo una función para validar la fecha. De tal forma que al leer una fecha se asegura que es válida.

Crear un programa que utilizando las funciones anteriores muestre el siguiente menú:
Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado.
Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.
Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra la producto.
Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la cociente.
Salir

"""


def SumaFraccion():
    try:
        n01 = int(input("Ingrese el numerador de la fraccion 1: "))
        d01 = int(input("Ingrese el denominador de la fraccion 1: "))
        n02 = int(input("Ingrese el numerador de la fraccion 2: "))
        d02 = int(input("Ingrese el denominador de la fraccion 2: "))
        fr01 = Fraction(n01, d01)
        fr02 = Fraction(n02, d02)
        print(f"La suma es: {fr01 + fr02}")
    except Exception as e:
        print("Los vlaores ingresados no son admitidos..")


def RestaFraccion():
    try:
        n01 = int(input("Ingrese el numerador de la fraccion 1: "))
        d01 = int(input("Ingrese el denominador de la fraccion 1: "))
        n02 = int(input("Ingrese el numerador de la fraccion 2: "))
        d02 = int(input("Ingrese el denominador de la fraccion 2: "))
        fr01 = Fraction(n01, d01)
        fr02 = Fraction(n02, d02)
        print(f"La suma es: {fr01 - fr02}")
    except Exception as e:
        print("Los vlaores ingresados no son admitidos..")


def MultiFraccion():
    try:
        n01 = int(input("Ingrese el numerador de la fraccion 1: "))
        d01 = int(input("Ingrese el denominador de la fraccion 1: "))
        n02 = int(input("Ingrese el numerador de la fraccion 2: "))
        d02 = int(input("Ingrese el denominador de la fraccion 2: "))
        fr01 = Fraction(n01, d01)
        fr02 = Fraction(n02, d02)
        print(f"La suma es: {fr01 * fr02}")
    except Exception as e:
        print("Los vlaores ingresados no son admitidos..")


def DivFraccion():
    try:
        n01 = int(input("Ingrese el numerador de la fraccion 1: "))
        d01 = int(input("Ingrese el denominador de la fraccion 1: "))
        n02 = int(input("Ingrese el numerador de la fraccion 2: "))
        d02 = int(input("Ingrese el denominador de la fraccion 2: "))
        fr01 = Fraction(n01, d01)
        fr02 = Fraction(n02, d02)
        print(f"La suma es: {fr01 / fr02}")
    except Exception as e:
        print("Los vlaores ingresados no son admitidos..")

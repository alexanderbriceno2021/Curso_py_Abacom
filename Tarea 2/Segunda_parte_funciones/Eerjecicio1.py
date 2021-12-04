"""
 Realiza una función llamada area_rectangulo() que devuelva el área del rectangulo a
 partir de una base y una altura.  Calcula el área de un rectángulo de 15 de base y 10 de altura.
"""

# solucion  1

base = 15
altura = 10


def area():
    print("El area del retangulo es: ", base * altura)


area()

# soluacion 2


def area_retangulo(base, altura):
    return base * altura


print("El area es: ", area_retangulo(15, 10))

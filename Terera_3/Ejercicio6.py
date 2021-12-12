"""
Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.
"""
from math import pi


def areaPerimetroCircunferencia():
    try:
        radio = float(
            input("Por favor digite el radio de la circulo: "))
        areaC = (radio ** 2) * pi
        periC = radio * 2 * pi
        print(f"El area es: {round(areaC,4)}")
        print(f"El permitero es: {round(periC,4)}")
    except Exception as e:
        print("El valor no ingresado no es valido")

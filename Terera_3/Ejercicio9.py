"""
Crear una función que calcule el MCD de dos número por el método de Euclides. El método de Euclides es el siguiente:

Se divide el número mayor entre el menor.
Si la división es exacta, el divisor es el MCD.
Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
Crea un programa principal que lea dos números enteros y muestre el MCD.
"""


def Mcd():
    try:
        num_may = int(input("Escriba el número mayor: "))
        num_men = int(input("Escriba el número menor: "))
        resto = 0
        if num_men > num_may:
            num_men, num_may = num_may, num_men
        while num_may % num_men != 0:
            num_men, num_may = num_may % num_men, num_men
        print(f"El MCD es: {num_men}")
    except Exception as e:
        print("El valor ingresado es erroneo")

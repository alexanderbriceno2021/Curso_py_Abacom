"""
Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y 
mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.
"""


def TemperaturaMedia():
    try:
        num_dias = int(
            input("Por favor digite el numero de dias a calcular: "))
        tem_max = 0
        tem_min = 1000
        tem_aux = 0
        for cont in range(1, num_dias+1):
            tem_aux = int(input(f"Temperatura dia {cont}: "))
            tem_max = max(tem_max, tem_aux)
            tem_min = min(tem_min, tem_aux)
        print(f"La temperatura maxima es: {tem_max}")
        print(f"La temperatura minima es: {tem_min}")
        print(f"La temperatura media es: {(tem_max + tem_min) / 2}")
    except Exception as e:
        print("Los valores ingresados no son enteros, error: ", type(e).__name__)

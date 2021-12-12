"""
Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

"""


def EsMultiplo():
    try:
        num1 = int(input("Por favor digite el primer numero: "))
        num2 = int(input("Por favor digite el segurndo numero: "))
        if num1 % num2 == 0:
            print(f"El numero", num1, "es multiplo de", num2)
        else:
            print(f"El numero", num1, "NO es multiplo de", num2)
    except Exception as e:
        print("Los valores ingresados no son enteros, error: ", type(e).__name__)

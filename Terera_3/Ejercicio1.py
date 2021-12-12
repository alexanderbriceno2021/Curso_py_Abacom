"""
Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla
(suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 espacios antes del texto).
Además subraya el mensaje utilizando el carácter =.
"""


def EscribirCentrado():
    cadena = input("Por favor escriba una cadena: ")
    columnas = 80
    aux = (columnas - len(cadena)) // 2
    espacios = " " * aux
    print(espacios+cadena)

"""
Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena con 
un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. 
Crea un programa principal donde se use dicha función.
"""
# Metodo 1


"""def ConvertirEspaciado():
    cadena = input("Por favor digite la cadena: ")
    print("Cadena Inicial: \n", cadena)
    print("Resultado de la Cadena: \n", " ".join(cadena))"""


# ConvertirseEspaciado()

# Metodo 2


def ConvertirEspaciado(cad):
    cad_espacio = cad.replace("", " ")
    cad_espacio.strip()
    return cad_espacio

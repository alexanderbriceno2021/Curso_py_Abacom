"""
Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, 
pero no debe repetise ningún elemento en la nueva lista:
"""
lista_1 = [1, 2, 3, 4, "Maria", "Alex", 5, 6, 7, 8, 9, "Danni"]

lista_2 = ["Alex", "fran", "Maria", "pepe"]

lista_3 = []

for x in lista_1:
    if x in lista_1 and x in lista_2:
        lista_3.append(x)

print("los elementos repetidos son: ", lista_3)

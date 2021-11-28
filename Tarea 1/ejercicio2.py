"""
EJERCICIO 2.- Calcular el perímetro y área de un círculo dado su radio

"""

import math

radio = float(input("Dime el radio: "))
print("Resultado: Area= %.2f Perimetro= %.2f" %
      (math.pi*radio**2, 2*math.pi*radio))

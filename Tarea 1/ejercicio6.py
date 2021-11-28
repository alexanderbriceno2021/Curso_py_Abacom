"""
EJERCICIO 6.- Calcular el área y el perímetro de un Rectángulo

Formula
Área: altura * ancho
Perímetro: (altura + ancho) * 2
"""
# Solucion Sencilla

altura = float(input("Dime la altura:"))
ancho = float(input("Dime la base:"))

area = ancho * altura
perimetro = 2*altura + 2*ancho

print("Resultado: Area= %.2f Perimetro= %.2f" % (area, perimetro))


# Solucion con funciones

print("Solucion con funciones")

altura = float(input("Dame la Altura por favor: "))
ancho = float(input(" Dame el ancho por favor: "))


def area():
    print("El Area es :", altura*ancho)


area()


def perimetro():
    print("El Perimetro es: ", (altura + ancho)*2)


perimetro()

import fractions
from math import pi, trunc
from os import system, name
from fractions import Fraction
from tkinter.constants import X
from Todos_ejercicos import CalcularMaxMin, ConvertirEspaciado, DiaJuliano, DivFraccion, EsMultiplo, EscribirCentrado, Factorial, Login, Mcd, MultiFraccion, RestaFraccion, SumaFraccion, TemperaturaMedia, areaPerimetroCircunferencia
import Ejercicio1
import Ejercicio2
import Ejercicio3
import Ejercicio4
import Ejercicio5
import Ejercicio6
import Ejercicio7
import Ejercicio8
import Ejercicio9
import Ejercicio10
import Ejercicio11
import Ejercicio12
import Ejercicio13
# Crear un programa que muestre un Menú Interactivo
# con los siguientes ejercicios:

# PROGRAMA PRINCIPAL


def MenuPrincipal():
    """Clase que nos presenta el menu principal
    Returns:
        op = devuelve la opcion seleccionada
    """

    print('''
          =======================================
          \tMENU PRINCIPAL
          =======================================
          1.\tEscribir Centrado
          2.\tEs Multiplo
          3.\tTemperatura Media
          4.\tConvertir espaciado
          5.\tCalcular Maximo y Minimo
          6.\tCalcular area y permitro de una Circunferencia
          7.\tLogin
          8.\tFactorial de un numero
          9.\tCalcular MCD
          10.\tCalculo de segundos y horas
          11.\tDia Juliano
          12.\tValidar Fecha
          13.\tFracciones
          X.\tSALIR
          ''')
    op = input("Por favor digite su opcion: ")
    return op


def MenuHoras():
    print(".:Calculos de segundos y horas:.")
    print("\t1. Horas a segundos")
    print("\t2. Segundos a horas")
    print("\tX. Retornar Menu Principal")
    oph = input("Seleccione su opcion: ")
    return oph


def MenuFracciones():
    print(".:Operaciones con Fracciones:.")
    print("\t1. Suma")
    print("\t2. Resta")
    print("\t3. Multiplicacion")
    print("\t4. Division")
    print("\tX. Retornar Menu Principal")
    opf = input("Seleccione su opcion: ")
    return opf


def borrarPantalla():
    if name == "posix":
        system("clear")
    elif ((name == "ce" or name == "nt") or name == "dos"):
        system("cls")


activo = True
while activo:
    resp = MenuPrincipal()
    print("\n")
    if resp == "1":
        borrarPantalla()
        print(".:Escribir Centrado:.")
        EscribirCentrado()
    elif resp == "2":
        borrarPantalla()
        print(".:Validar Multiplo:.")
        EsMultiplo()
    elif resp == "3":
        borrarPantalla()
        print(".:Temperatura Media:.")
        TemperaturaMedia()
    elif resp == "4":
        borrarPantalla()
        print(".:Convertir espaciado:.")
        palabra = input("Introduce una palbra: ")
        print("El texto espaciado:", ConvertirEspaciado(palabra))
        ConvertirEspaciado(palabra)
    elif resp == "5":
        borrarPantalla()
        print(".:Calcular Maximo y Minimo:.")
        num = input(
            "Digite los valores numéricos de la lista, separada por , (coma): ")
        lista_valores = list(map(int, num.split(',')))
        CalcularMaxMin(lista_valores)
    elif resp == "6":
        borrarPantalla()
        print(".:Calcular Area y Perimetro de la Circunferencia:.")
        areaPerimetroCircunferencia()
    elif resp == "7":
        borrarPantalla()
        print(".:Validacion de credenciales:.")
        Login()
    elif resp == "8":
        borrarPantalla()
        print(".:Calcular el factorial de un numero:.")
        Factorial()
    elif resp == "9":
        borrarPantalla()
        print(".:Calcular el MCD de 2 numeros:.")
        Mcd()
    elif resp == "10":
        borrarPantalla()
        while True:
            op10 = MenuHoras()
            if op10 == "1":
                print(".::Horas a Segundos::.")
                TiempoSegundos()
            elif op10 == "2":
                print(".::Segundos a Horas::.")
                SegundosTiempo()
            elif (op10 == "X" or op10 == "x"):
                borrarPantalla()
                break
    elif resp == "11":
        borrarPantalla()
        print(".:Calculo del Dia Juliano:.")
        DiaJuliano()
    elif resp == "12":
        borrarPantalla()
        try:
            print(".:Valida Fecha:.")
            yy = int(input("Digite el año: "))
            mm = int(input("Digite el mes: "))
            dd = int(input("Digite el dia: "))
            if ValidaFecha(dd, mm, yy):
                print(f"La fecha ingresada es correcta: {dd}/{mm}/{yy}")
            else:
                print(f"La fecha ingresada no es correcta: {dd}/{mm}/{yy}")
        except Exception as e:
            print("Los valores ingresados no son admitidos..")
    elif resp == "13":
        borrarPantalla()
        while True:
            op13 = MenuFracciones()
            if op13 == "1":
                print(".::Suma de fracciones::.")
                SumaFraccion()
            elif op13 == "2":
                print(".::Resta de fracciones::.")
                RestaFraccion()
            elif op13 == "3":
                print(".::Multipliacion de fracciones::.")
                MultiFraccion()
            elif op13 == "4":
                print(".::Division de fracciones::.")
                DivFraccion()
            elif (op13 == "X" or op13 == "x"):
                borrarPantalla()
                break
    elif (resp == "X" or resp == "x"):
        borrarPantalla()
        activo = False
    else:
        print("Digite un opcion valida...")
print("Gracias, Ejecución exitosa!!!")

# Crear un programa que muestre un Menú Interactivo
# con los siguientes ejercicios:

import fractions
from math import pi, trunc
from os import system, name
from fractions import Fraction
from tkinter.constants import X


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


# Ejercicio 01
def EscribirCentrado():
    cadena = input("Por favor Escriba una palabra: ")
    columnas = 80
    aux = (columnas - len(cadena)) // 2
    espacios = " " * aux
    print(espacios+cadena)

# Ejercicio 02


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

# Ejercicio 03


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
        print("La temperatura maxima es: ", tem_max)
        print("La temperatura minima es: ", tem_min)
        print("La temperatura media es: ", (tem_max + tem_min) / 2)
    except Exception as e:
        print("Los valores ingresados no son enteros, error: ", type(e).__name__)

# Ejercicio 04


def ConvertirEspaciado(cad):
    cad_espacio = cad.replace("", " ")
    cad_espacio.strip()
    return cad_espacio

# Ejercicio 05


def CalcularMaxMin(lista_num):
    num_max = 0
    num_min = 1000
    for i, dato in enumerate(lista_num):
        num_max = max(num_max, dato)
        num_min = min(num_min, dato)
    print(f"La lista de numeros es: {lista_num}")
    print(f"El valor maximo es: {num_max}")
    print(f"El valor minimo es: {num_min}")

# Ejercicio 06


def areaPerimetroCircunferencia():
    try:
        radio = float(
            input("Por favor digite el radio de la circulo: "))
        areaC = (radio ** 2) * pi
        periC = radio * 2 * pi
        print(f"El area es: {round(areaC,4)}")
        print(f"El permitero es: {round(periC,4)}")
    except Exception as e:
        print("El valor ingresado no es valido")

# Ejercicio 07


def Login():
    usuario = "usuario1"
    clave = "asdasd"
    intento = 1
    while intento <= 3:
        usr_aux = input("Escriba su usuario: ")
        pas_aux = input("Escriba su clave: ")
        if (usuario == usr_aux and clave == pas_aux):
            print("Acceso correcto!!")
            return
        else:
            print("Usuario o contraseña incorrectas, intente de nuevo!!")
            intento += 1
    if intento > 3:
        print("Ha superado los intentos permitidos, intentelo mas tarde.")


# Ejercicio 08
def Factorial():
    try:
        num = int(input("Digite el número a calcular: "))
        aux = 1
        for factor in range(1, num+1):
            aux = factor * aux
        print(f"El factorial de {num} es:", aux)
    except Exception as e:
        print("El valor ingresado es erroneo")

# Ejercicio 09


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

# Ejercicio 10


def TiempoSegundos():
    try:
        hora = int(input("Ingrese las horas: "))
        min = int(input("Ingrese los minutos: "))
        seg = int(input("Ingrese los segundos: "))
        seg01 = seg + (min * 60) + (hora*3600)
        print(
            f"Los datos ingresados (hh:mm:ss): {hora}:{min}:{seg} dan {seg01} segundos")
    except Exception as e:
        print("Los datos ingresados no son admitidos..")


def SegundosTiempo():
    try:
        segs = int(input("Ingrese los segundos: "))
        auxseg = 0
        if segs >= 3600:
            horas = segs // 3600
            auxseg = segs % 3600
            mins = auxseg // 60
            auxseg = auxseg % 60
            print(
                f"Los segundos ingresados {segs} da (hh:mm:ss): {horas}:{mins}:{auxseg}")
        elif (segs >= 60 and segs < 3600):
            horas = 0
            mins = auxseg // 60
            auxseg = auxseg % 60
            print(
                f"Los segundos ingresados {segs} da (hh:mm:ss): {horas}:{mins}:{auxseg}")
        elif (segs >= 0 and segs < 60):
            horas = 0
            mins = 0
            print(
                f"Los segundos ingresados {segs} da (hh:mm:ss): {horas}:{mins}:{segs}")
        else:
            print("Datos no ingresados erroneos")
    except Exception as e:
        print("Los datos ingresados no son admitidos..")

# Ejercicio 12


def AnioBisiesto(anio):
    if anio % 4 != 0:
        return False
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0:
        return False
    elif anio % 4 == 0 and anio % 100 != 0:
        return True
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0:
        return True


def ValidaFecha(dd, mm, aa):
    lista_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if AnioBisiesto(aa):
        lista_mes[1] = 29

    if len(str(aa)) == 4:
        if mm in range(1, 12):
            if (dd > 0 and dd <= lista_mes[mm-1]):
                return True
    else:
        return False

# Ejercicio 11


def DiaJuliano():
    anio = int(input("Ingrese el año: "))
    mes = int(input("Ingrese el mes: "))
    dia = int(input("Ingrese el dia: "))
    if ValidaFecha(dia, mes, anio):
        jd = (365.25*(anio+4716)) + (30.6001*(mes+1)) + \
            dia + (2 - (3*anio / 400)) - 1524.5
        print(f"La fecha juliana es: {int(jd)}")
    else:
        print("La fecha ingresada es erronea..")

# Ejercicio 13


def SumaFraccion():
    try:
        n01 = int(input("Ingrese el numerador de la fraccion 1: "))
        d01 = int(input("Ingrese el denominador de la fraccion 1: "))
        n02 = int(input("Ingrese el numerador de la fraccion 2: "))
        d02 = int(input("Ingrese el denominador de la fraccion 2: "))
        fr01 = Fraction(n01, d01)
        fr02 = Fraction(n02, d02)
        print(f"La suma es: {fr01 + fr02}")
    except Exception as e:
        print("Los vlaores ingresados no son admitidos..")


def RestaFraccion():
    try:
        n01 = int(input("Ingrese el numerador de la fraccion 1: "))
        d01 = int(input("Ingrese el denominador de la fraccion 1: "))
        n02 = int(input("Ingrese el numerador de la fraccion 2: "))
        d02 = int(input("Ingrese el denominador de la fraccion 2: "))
        fr01 = Fraction(n01, d01)
        fr02 = Fraction(n02, d02)
        print(f"La suma es: {fr01 - fr02}")
    except Exception as e:
        print("Los vlaores ingresados no son admitidos..")


def MultiFraccion():
    try:
        n01 = int(input("Ingrese el numerador de la fraccion 1: "))
        d01 = int(input("Ingrese el denominador de la fraccion 1: "))
        n02 = int(input("Ingrese el numerador de la fraccion 2: "))
        d02 = int(input("Ingrese el denominador de la fraccion 2: "))
        fr01 = Fraction(n01, d01)
        fr02 = Fraction(n02, d02)
        print(f"La suma es: {fr01 * fr02}")
    except Exception as e:
        print("Los vlaores ingresados no son admitidos..")


def DivFraccion():
    try:
        n01 = int(input("Ingrese el numerador de la fraccion 1: "))
        d01 = int(input("Ingrese el denominador de la fraccion 1: "))
        n02 = int(input("Ingrese el numerador de la fraccion 2: "))
        d02 = int(input("Ingrese el denominador de la fraccion 2: "))
        fr01 = Fraction(n01, d01)
        fr02 = Fraction(n02, d02)
        print(f"La suma es: {fr01 / fr02}")
    except Exception as e:
        print("Los vlaores ingresados no son admitidos..")


"""# PROGRAMA PRINCIPAL
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
        ConvertirEspaciado()
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
print("Gracias, Ejecución exitosa!!!")"""

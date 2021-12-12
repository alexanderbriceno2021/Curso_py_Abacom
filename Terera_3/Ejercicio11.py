"""
El día juliano correspondiente a una fecha es un número entero que indica los días que han transcurrido desde el 1 de enero del año indicado. Queremos crear un programa principal que al introducir una fecha nos diga el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:

LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
EsBisiesto: Recibe un año y nos dice si es bisiesto.
Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.
"""


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

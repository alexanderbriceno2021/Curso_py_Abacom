"""
Vamos a mejorar el ejercicio anterior haciendo una función para validar la fecha. 
De tal forma que al leer una fecha se asegura que es válida.
"""


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

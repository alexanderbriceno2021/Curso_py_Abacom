"""
Escribir dos funciones que permitan calcular:

La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas,minutos y segundos o salir del programa
"""


def TiempoSegundos():
    try:
        hora = int(input("Ingrese las horas: "))
        min = int(input("Ingrese los minutos: "))
        seg = int(input("Ingrese los segundos: "))
        seg01 = seg + (min * 60) + (hora*3600)
        print(
            f"Los Datos ingresados (hh:mm:ss): {hora}:{min}:{seg} dan {seg01} segundos")
    except Exception as e:
        print("Los Datos ingresados no son admitidos..")


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
            print("Valores ingresados erroneos")
    except Exception as e:
        print("Los datos ingresados no son admitidos..")

"""
Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además 

"""


def Login():
    usuario = "usuario1"
    clave = "asdasd"
    intento = 1
    while intento <= 3:
        usr = input("Escriba su usuario: ")
        pasw = input("Escriba su clave: ")
        if (usuario == usr and clave == pasw):
            print("Acceso correcto!!")
            return
        else:
            print("Usuario o contraseña incorrectas, intente de nuevo!!")
            intento += 1
    if intento > 3:
        print("Ha superado los intentos permitidos, Adios")

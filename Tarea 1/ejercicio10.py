"""
EJERCICIO 10.- Escribe un programa que pida un nombre de usuario y una contraseña 
y si se ha introducido “pepe” y “passwd#” se indica “Has entrado al sistema”, sino se da un error.
"""
usuario = input("Coloque nombre de usuario: ")
contraseña = input("Coloque su contraseña: ")

if usuario=="pepe" or contraseña=="passwed#":
    print("Has esntrado al sistema")
else:
    print(" Error, Usuario o contraseña incorrectas")
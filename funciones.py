import re


def imprimeDato(*nombre):
    print(f"El nombres es: {list(nombre)}")

def nombreCompleto(apellido, nombre):
    print(f"El nombres es: {nombre} {apellido}")
    
def nombreCompleto2(**kwargs):
    print(f"El nombres es: {kwargs['nombre']} {kwargs['apellido']}")
    
def miFuncion2(argumento= "Hola"):
    print(argumento)
    
def miFuncionLista(lista):
    for elemento in lista:
        print(elemento)

def concatenaNombre(lista):
    i = ""
    for elemento in lista:
        i = i + elemento + " "
    return i

def recursion(i):
    if (i < 1):
        return i
    print(i)
    recursion(i-1)

if __name__ == "__main__":
    #imprimeDato("Sebastian", "Allende",24)
    #nombreCompleto2(nombre="Sebastian", apellido="Allende")
    #miFuncion2("Seba")
    nombres = concatenaNombre(["Seba", "Allende", "24"])
    print(nombres)
    recursion(10)
     
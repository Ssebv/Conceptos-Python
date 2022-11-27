
hola = "hola"

if hola == "hola":
    print("Hola Mundo")

if 5 > 4:
    print("Si es mayor")

# Hola esto es un comentario

# Numeral

var_1 = 1


a , b , c = "lala" , "lolo" , "lili"

print(a, b, c)

valor1 = valor2 = valor3 = "Todas contiene el mismo valor"

print(valor1, valor2, valor3, sep="\n")

inicio = "Hola"
final = "Mundo"
espacio = " "

print(inicio + espacio + final)
print(inicio, final)

palabra = 'Hola Mundo' # Esto es un string 
palabra2 = "Hola Mundo"

entero = 5435 #integer
flotante = 4.5 #float
complejo = 2j #complex 

print(entero, flotante, complejo, palabra2)

lista = [1,2,3,4,5]
numeros = 1, 2, 3, 4, 5 # tupla
print(type(numeros))
lista2 = lista.copy()

lista.append(2)
lista.append(3)


print(lista)
print(lista2)
print(lista + lista2)
print(lista * 3)
print(lista, lista2.count(2))
print(lista.count(2))

print(len(lista))
print(lista.index(2))
lista.pop(0)
lista.remove(2)
lista.reverse()

print(lista)
lista.sort()
print(lista)
#lista.clear()

lista3 = [1,24,1,54,1,4,2]

for i in range(0,3):
    lista3.append("hola")
    
lista3.append("pepe")
print(lista3[3])
print(lista3)
lista3.remove(1)
print(lista3)
lista3.reverse()
print(lista3)
#lista3.sort()

lista4 = [1,43,4,2,1,33,4,123,121,2,1]
lista5 = ["a","x","b","c","d","e","f","g","h","i","j"]
lista4.sort()
lista5.sort()
print(lista4)
print(lista5)

tupla = ("hola", "mundo", "somos", "tuplas")
listaDeTupla = list(tupla)
print(tupla)
print(tupla.count("hola"))
print(tupla.index("somos"))
print(tupla[1])
print(listaDeTupla)

rango = range(5)
print(rango)

diccionario = {
    "nombre": "pepe", 
    "apellido": "perez", 
    "edad": 23
}

print(diccionario)
print(diccionario["nombre"])
print(diccionario["apellido"])
print(diccionario.get("nombre"))
diccionario["nombre"] = "juan"
print(diccionario.get("nombre"))
print(len(diccionario))

diccionario["Rut"] = 202234567
print(diccionario)
#diccionario.pop("edad")
diccionario.popitem() # Elimina el ultimo elemento que se agrego
print(diccionario)
copia = diccionario.copy()
copia2 = dict(diccionario)
del diccionario["edad"]
print(diccionario)
print(copia)
diccionario.clear()

print(copia2)
print(diccionario, copia)

Tom = {
        "nombre": "Tom",
        "edad": 4
    }
Pelusa = {
     "nombre": "Pelusa",
        "edad": 14
}
diccionario2 = {
    "Tom": Tom,
    "Pelusa": Pelusa
       
    
}

print(diccionario2["Tom"])

perritos = dict(nombre="Negra", edad=3)
print(perritos)

boleano = True
boleano2 = False #bool

print(type(boleano))

print(boleano, boleano2)







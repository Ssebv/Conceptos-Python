numero1 = input("Ingrese el primer numero: ")

numero2 = input("Ingrese el segundo numero: ")


try:
    numero1 = int(numero1)
except:
    numero1 = "No es un numero"
    
try:
    numero2 = int(numero2)
except:
    numero2 = "No es un numero"

if numero1 == "No es un numero" or numero2 == "No es un numero":
    print("Debe de ingresar solo numeros")
    exit()

# print(numero1, numero2)


simbolo = input("Ingrese la operacion de operacion: ")

if simbolo == "*":
    operacion = numero1 * numero2
    print(f"El resultado de la operacion {numero1} {simbolo} {numero2} es: {operacion}")
elif simbolo == "/":
    operacion = numero1 / numero2
    print(f"El resultado de la operacion {numero1} {simbolo} {numero2} es: {operacion}")
elif simbolo == "+":
    operacion = numero1 + numero2
    print(f"El resultado de la operacion {numero1} {simbolo} {numero2} es: {operacion}")
elif simbolo == "-":
    operacion = numero1 - numero2
    print(f"El resultado de la operacion {numero1} {simbolo} {numero2} es: {operacion}")
elif simbolo == "**":
    operacion = numero1 ** numero2
    print(f"El resultado de la operacion {numero1} {simbolo} {numero2} es: {operacion}")
elif simbolo == "//":
    operacion = numero1 // numero2
    print(f"El resultado de la operacion {numero1} {simbolo} {numero2} es: {operacion}")
elif simbolo == "%":
    operacion = numero1 % numero2
    print(f"El resultado de la operacion {numero1} {simbolo} {numero2} es: {operacion}")
else:
    print(f"Simbolo {simbolo} es invalido")

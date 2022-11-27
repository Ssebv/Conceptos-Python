#i = 0

#while i<11:
#    i += 1
#    if i == 3:
#       continue
#    print(i)
    
from calendar import c


usuarios = ["admin", "root", "user", "guest"]

for usuario in usuarios:
    if usuario == "root":
        continue
    print(usuario)

#usuario = input("Ingrese su usuario: ")

#for c in usuario:
    #print(c)
    
for x in range(0,33,3):
    print(x)
else:
    print("Fin del ciclo")
    
    
usuarios = ["admin", "root", "user", "guest"]

edades = [20, 30, 40, 50]

for usuario in usuarios:
    for edad in edades:
        print(usuario, edad)
        
def miFuncion():
    print("Hola")
    
miFuncion()
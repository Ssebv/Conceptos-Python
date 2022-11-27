
class Usuario:
    def __init__(self, nombre,apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludar(self):
        print("Hola, soy", self.nombre)

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")
        
class Admin(Usuario):
    def supersaludo(self):
        print("Hola, soy", self.nombre, "y soy admin")
      
usuario1 = Usuario("Juan","Vegas",17)
usuario2 = Usuario("Esteban", "Vegas", 18)

print("El primer usuario es " + usuario1.apellido + "\n" +"El segundo usuario es " + usuario2.nombre)
print(
    (f"El primer usuario es {usuario1.nombre} {usuario1.apellido}" +  "\n" + 
     f"El segundo usuario es {usuario2.nombre} {usuario2.apellido}")
    )

admin = Admin("Sebastian", "Allende", 24)

admin.saludar()
admin.supersaludo()

#usuario1.saludar()
#usuario2.saludar()

#usuario1.nombre = "Sebastian"
#usuario1.saludar()

#del usuario1
#print(usuario1)

#usuario1 = Usuario("Esteban", "Vegas", 18)
#usuario1.saludar()
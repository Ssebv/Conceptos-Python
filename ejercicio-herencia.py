class Animal:
    def __init__(self,animal, nombre, onomatopeya):
        self.animal = animal
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print(f"Hola, soy {self.nombre} un {self.animal} y mi sonido es {self.onomatopeya}")

class Gato(Animal):
    
    def __init__(self,animal, nombre, onomatopeya):
        Animal.__init__(self,animal, nombre, onomatopeya)
        print(f"Hola, soy {self.nombre} un {self.animal} extendido")
        
class Perro(Animal):
    def __init__(self,animal, nombre, onomatopeya):
        super().__init__(animal, nombre, onomatopeya)
        print("Instanciando un perro")

gato = Gato("Gato","Fato", "Miauu")
perro = Perro("Perro","Firulais", "Guauu")

#gato.saludo()
#perro.saludo()
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def ladrar(self):
        print("¡Guau!")

class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def mostrarAtributos(self):
        print(self.nombre + "\t" + str(self.dni), end="\t")

class Cliente(Persona):
    def __init__(self, nombre, dni, perro):
        Persona.__init__(self, nombre, dni)
        self.perro = perro
    def mostrarAtributos(self):
        super().mostrarAtributos()
        print(self.perro.nombre + "\t" + self.perro.raza)


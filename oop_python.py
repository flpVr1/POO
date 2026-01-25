class Personaje:
    # Contructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        # Atributos
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    # Atributos del personaje.
    def atributos(self):
        print(self.nombre, ":", sep=" ")
        print("• Fuerza:", self.fuerza)
        print("• Inteligencia:", self.inteligencia)
        print("• Defensa:", self.defensa)
        print("• Vida:", self.vida)

    # Metodo para subir de nivel a las estadísticas del personaje
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    # Metodo para indicar si el personaje esta vivo (True) o muerto (False)
    def esta_vivo(self):
        return self.vida > 0
    
    # Metodo para indicar si el personaje está vivo o muerto
    def morir(self):
        self.vida = 0
        print(self.nombre, "Ha muerto")

    # Metodo para hacer daño de acuerdo a la defensa del enemigo
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    # Metodo para atacar
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida del personaje", enemigo.nombre, "es", enemigo.vida)
        else:
            return enemigo.morir()
        
    # Metodos setters y getters
    # El metodo get sirve para obtener un valor en particular y tener un mayor control de los métodos creados
    def get_fuerza(self):
        return self.fuerza
    
    # El método set establece el valor que recibirá get y lo dobreescribirá por sobre lo ya establecido
    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print('Error, haz ingresado un número negativo, intenta nuevamente')
        else:
            self.fuerza = fuerza

# Herencias
"""
Las herencias son sumamente importantes ya que 
ayudan a no escribir código repetitivo y hacer todo
un poco más rápido a la hora de codificar
"""

class Guerrero(Personaje): # La herencia parte al momento de especificar entre parétesis de quien se van a heredar los métodos y atributos, que es de la clase Personaje.

    # Para agregar un atributo adicional (Espada) a la Herencia en Guerrero se debe sobreescribir el constructor del Personaje.
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada


class Mago(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

goku = Personaje('Goku', 10, 5, 5, 100)
goku.atributos()
guts = Guerrero('Guts', 20, 4, 7, 100, 5)
guts.atributos()
print(guts.espada)
barbara = Mago('Bárbara', 8, 15, 6, 100, 8)
barbara.atributos()
print(barbara.libro)
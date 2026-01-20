class Personaje:
    # Contructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        # Atributos
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep=" ")
        print("• Fuerza:", self.fuerza)
        print("• Inteligencia:", self.inteligencia)
        print("• Defensa:", self.defensa)
        print("• Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "Ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida del personaje", enemigo.nombre, "es", enemigo.vida)
        else:
            return enemigo.morir()

mi_personaje = Personaje('Felipe', 10, 1, 5, 100)
mi_enemigo = Personaje("Enemigo Stando", 8, 5, 3, 5)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()
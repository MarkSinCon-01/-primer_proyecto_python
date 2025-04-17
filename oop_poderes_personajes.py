class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(f"\n{self.__class__.__name__}")
        print(f"• Nombre: {self.nombre}")
        print(f"• Fuerza: {self.fuerza}")
        print(f"• Inteligencia: {self.inteligencia}")
        print(f"• Defensa: {self.defensa}")
        print(f"• Vida: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(f"{self.nombre} ha muerto.")

    def daño(self, enemigo):
        return max(self.fuerza - enemigo.defensa, 0)

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(f"\n{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}")
        if enemigo.esta_vivo():
            print(f"La vida de {enemigo.nombre} es {enemigo.vida}")
        else:
            enemigo.morir()


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def atributos(self):
        super().atributos()
        print(f"• Espada: {self.espada}")

    def daño(self, enemigo):
        return max((self.fuerza + self.espada) - enemigo.defensa, 0)


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print(f"• Libro: {self.libro}")

    def daño(self, enemigo):
        return max((self.inteligencia + self.libro) - enemigo.defensa, 0)


# 🔹 Creación de personajes y muestra de atributos en una sola ejecución
guts = Guerrero("Guts", 20, 10, 10, 100, espada=5)
goku = Personaje("Goku", 20, 15, 10, 100)
vanessa = Mago("Vanessa", 20, 15, 10, 100, libro=5)

guts.atributos()
goku.atributos()
vanessa.atributos()

# 🔹 Simulación de ataques
print("\n--- COMBATE ---")
goku.atacar(guts)
guts.atacar(vanessa)
vanessa.atacar(goku)
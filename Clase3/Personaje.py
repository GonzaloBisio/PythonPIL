class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def atacar(self):
        print(self.nombre, 'está atacando')

    def recibir_daño(self):
        self.vida - 20

class Centinela(Personaje):
    def __int__(self, funcion, habilidad):
        self.funcion = 'Centinela'
        self.habilidad = 'Curar'

    def curar(self):
        print('Te ha curado',self.nombre)


centinela1 = Centinela('Sage',100)

print(centinela1.nombre, centinela1.vida)
centinela1.curar()
centinela1.atacar()
centinela1.recibir_daño()


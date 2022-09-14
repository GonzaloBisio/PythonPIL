class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad


class Perro(Animal):

    def __init__(self, nombre, raza):
        super().__init__(especie, edad)
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print('Guau')

    def jugar(self, objeto):
        print('Jugando con', objeto)

    def saludar(self):
        print('Hola, mi nombre es', self.nombre)


perro1 = Perro('Marcos', 'Collie', 'Perro', 5)

print(f'Perro 1 -> {perro1.raza}, {perro1.nombre}, {perro1.edad}')

perro1.jugar('pelota')

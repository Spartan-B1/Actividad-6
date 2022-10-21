from particula import Particula


class Lista:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula: Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula: Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)


l0 = Particula(id=4, ox=5, oy=7.0, dx=5.0, dy=4.0)
l2 = Particula(102, 7, 8, 6, 4, 1, 6, 4, 1)

lista = Lista()

lista.agregar_inicio(l2)
lista.agregar_final(l0)

lista.mostrar()
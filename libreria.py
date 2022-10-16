from particula import Particula


class Libreria:
    def __init__(self):
        self._particulas = []

    def agregar_final(self, particula: Particula):
        self._particulas.append(Particula)

    def agregar_inicio(self, particula: Particula):
        self._particulas.insert(0, Particula)


    def mostrar(self):
        for Particula in self._particulas:
            print(Particula)
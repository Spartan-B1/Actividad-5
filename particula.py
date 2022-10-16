from algoritmos import distancia_euclidiana



class Particula:
    def __init__(self,
                 id="", origen_x="", origen_y="", destino_x="", destino_y="",
                 velocidad="", red="", green="", blue="", distancia=""):
        self._id = id
        self._origen_x = origen_x
        self._origen_y = origen_y
        self._destino_x = destino_x
        self._destino_y = destino_y
        self._velocidad = velocidad
        self._red = red
        self._green = green
        self._blue = blue
        self._distancia = distancia

    def __str__(self):
        return (
                'id: ' + self._id + '\n' +
                'origen_x: ' + self._origen_x +
                'origen_y: ' + self._origen_y +
                'destino_x: ' + self._destino_x +
                'destino_y: ' + self._destino_y +
                'velocidad: ' + self._velocidad +
                'red: ' + self._red +
                'green: ' + self._green +
                'blue: ' + self._blue +
                'distancia: ' + self._distancia
        )


self.distancia = distancia_euclidiana(origen_x, destino_x, origen_y, destino_y)

libreria = Libreria()
libreria.agregar_final(self.distancia)
libreria.agregar_inicio(self.distancia)
libreria.agregar_inicio(self.distancia)
libreria.mostrar()
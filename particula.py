
from algoritmos import distancia_euclidiana


class Particula:
    def __init__(self, id=0.0, ox=0.0, oy=0.0, dx=0.0, dy=0.0, vel=0.0, r=0, g=0, b=0):
        self.__id = repr(id)
        self.__origen_x = repr(ox)
        self.__origen_y = repr(oy)
        self.__destino_x = repr(dx)
        self.__destino_y = repr(dy)
        self.__velocidad = repr(vel)
        self.__red = repr(r)
        self.__green = repr(g)
        self.__blue = repr(b)
        self.__distancia = repr(distancia_euclidiana(ox, oy, dx, dy))
    
    def __str__(self):
        return(
            'ID: ' + self.__id + '\n' +
            'Origen X: ' + self.__origen_x + '\n' +
            'Origen Y: ' + self.__origen_y + '\n' +
            'Destino X: ' + self.__destino_x + '\n' +
            'Destino Y: ' + self.__destino_y + '\n' +
            'Velocidad: ' + self.__velocidad + ' M/S \n' +
            'Rojo: ' + self.__red + '\n' +
            'Verde: ' + self.__green + '\n' +
            'Azul: ' + self.__blue + '\n' +
            'Distancia: ' + self.__distancia + ' M \n' 
            )

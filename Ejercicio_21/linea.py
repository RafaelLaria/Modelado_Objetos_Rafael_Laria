from entidad import EntidadGeografica
from punto import Punto
class Linea(EntidadGeografica):
    def __init__(self, codigo, nombre, puntos):
        super().__init__(codigo, nombre)
        self.puntos = []

    def agregar_puntos(self, punto : Punto):
        self.puntos.append(punto)
        if self.puntos >= 2:
            return self.puntos
        else:
            raise ValueError('Una linea tiene como mínimo dos puntos')
    
    def __str__(self):
        coord = [p.dar_coordenadas() for p in self.puntos]
        return f'Linea {self.nombre} [{self.codigo}]: {coord}'
    
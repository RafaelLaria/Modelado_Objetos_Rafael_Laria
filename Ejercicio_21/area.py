from entidad import EntidadGeografica
from punto import Punto

class Area(EntidadGeografica):
    def __init__(self, nombre, codigo):
        super().__init__(nombre, codigo)
        self.puntos = []
    
    def agregar_puntos(self, punto : Punto):
        self.puntos.append(punto)
        if len(self.puntos) >= 3:
            return self.puntos
        else:
            raise ValueError('Un área debe tener mínimo tres puntos')
    
    def __str__(self):
        coord = [p.dar_coordenadas for p in self.puntos]
        return f'Area {self.nombre} [{self.codigo}]: {coord}'
    

from entidad import EntidadGeografica

class Punto(EntidadGeografica):
    def __init__(self, nombre, codigo):
        super().__init__(nombre, codigo)
        self.x = 0
        self.y = 0
        self.z = 0

    def dar_coordenadas(self):
        self.x = float(input('CoordenadaX: '))
        self.y = float(input('CoordenadaY: '))
        self.z = float(input('CoordenadaZ: '))
        return (self.x, self.y, self.z)

    def __str__(self):
        return f'Punto {self.nombre}[{self.codigo}]: ({self.x},{self.y},{self.z})'
    
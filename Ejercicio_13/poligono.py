class Poligono:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = []
    def __str__(self):
        return f'Polígono: {self.nombre}'
    
    def pertenece(self):
        for punto in self.puntos:
            return punto
    
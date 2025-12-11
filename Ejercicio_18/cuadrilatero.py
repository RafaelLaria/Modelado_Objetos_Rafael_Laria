from figura import Figura

class Cuadrilatero(Figura):
    def __init__(self, color):
        super().__init__(color)
        self.longitud = 0
        self.anchura = 0

    def dar_dimensiones(self):
        self.longitud = float(input('Longitud: '))
        self.anchura = float(input('Anchura: '))

    def que_es(self):
        resultado = 'Rectángulo'
        if self.longitud == self.anchura:
            resultado = 'Cuadrado'
            return resultado
        else:
            return resultado
    
    def __str__(self):
        return f'{self.que_es()}\n' \
               f'Longitud: {self.longitud}\n' \
               f'Anchura: {self.anchura}'
     

    
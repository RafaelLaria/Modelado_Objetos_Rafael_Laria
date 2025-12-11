from figura import Figura

class Conica(Figura):
    def __init__(self, color):
        super().__init__(color)
        self.eje_mayor = 0
        self.eje_menor = 0

    def dar_ejes(self):
        self.eje_mayor = float(input('Eje Mayor: '))
        self.eje_menor = float(input('Eje Menor: '))
    
    def que_es(self):
        resultado = 'Elipse'
        if self.eje_mayor == self.eje_menor:
            resultado = 'Círculo'
            return resultado
        else:
            return resultado
        
    def __str__(self):
        return f'{self.que_es()}\n' \
               f'Eje Mayor: {self.eje_mayor}\n' \
               f'Eje Menor: {self.eje_menor}'
    
     
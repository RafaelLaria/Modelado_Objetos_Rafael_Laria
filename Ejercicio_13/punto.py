from poligono import Poligono

class Punto:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def dar_puntos(self):
        while True:
            self.x = input('Coordenada X: ')
            self.y = input('Coordenada Y: ')
            punto = (self.x, self.y)
            self.puntos.append(punto)
            opcion = input('Desea continuar? \n' \
                           'a)Sí\n' \
                           'b)No')
            
            if opcion.lower() == 'a':
                continue
            elif opcion.lower() == 'b':
                print('Se usarán los puntos recibidos para construir el polígono')
                break
            else:
                print('Opción inválida')

    def a_que_pertenece(punto, figuras):
        for figura in figuras:
            if figura.pertenece(punto):
                return figura.nombre

if __name__ == '__main__':
    p1 = Poligono('Triángulo')
    p1.dar_puntos()

        

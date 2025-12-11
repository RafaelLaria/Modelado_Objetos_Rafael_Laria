class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

class Poligono:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = []

    def agregar_punto(self, punto):
        self.puntos.append(punto)
    
    def dar_puntos(self):
        while True:
            try:
                self.x = float(input('Coordenada X: '))
                self.y = float(input('Coordenada Y: '))
            except TypeError:
                print('Ecriba un número por favor')
                continue
            punto = Punto(self.x, self.y)
            self.agregar_punto(punto)
            opcion = input('Desea seguir creando puntos?:\n' \
                           'a)Sí\n' \
                           'b)No')
            if opcion.lower() == 'a':
                print('Se creará el polígono con los puntos recibidos')
                break
            elif opcion.lower() == 'b':
                print('Se continuará creando puntos')
                continue
            else:
                print('Por favor, escoja a o b')
            
    def pertenece(self, punto):
        for punto in self.puntos:
            return punto
    
def a_que_pertenece(punto, poligonos):
    for pol in poligonos:
        if pol.pertenece(punto):
            return pol.nombre

#Creación de puntos
poligonos = []
try:
    cantidad = int(input('¿Cuantos polígonos desea crear?: '))
except TypeError:
    print('Por favor escriba un número entero')

for i in range(cantidad):
    nombre = input('Nombre del polígono: ')
    pol = Poligono(nombre)
    pol.dar_puntos()
    poligonos.append(pol)

print('A que polígono pertenece cada punto creado\n')
x = float(input('CoordenadaX: '))
y = float(input('CoordenadaY: '))
p = Punto(x,y)
resultado = a_que_pertenece(p, poligonos)
print(f'El punto {p} pertenece a un {resultado}')
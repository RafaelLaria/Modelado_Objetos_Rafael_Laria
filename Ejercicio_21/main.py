from punto import Punto
from linea import Linea
from area import Area


p1 = Punto('A','1234')
p1.dar_coordenadas()
p2 = Punto('B','4321')
p2.dar_coordenadas()
p3 = Punto('C','1357')
p3.dar_coordenadas

l1 = Linea('Recta','2468')
l1.agregar_puntos(p1,p2)
a1 = Area('Circulo','9753')
a1.agregar_puntos(p1,p2,p3)

print(l1)
print(a1)
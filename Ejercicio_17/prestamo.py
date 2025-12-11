from libro import Libro
from ejemplar import Ejemplar

class Prestamo:
    plazo_maximo = 30
    def __init__(self, ejemplar, lector, dia_prestamo):
        self.ejemplar = ejemplar
        self.lector = lector
        self.dia_prestamo = dia_prestamo
        self.dia_entrega = dia_prestamo + self.plazo_maximo
        self.devuelto = False

    def devolucion(self):
        self.devuelto = True
        self.ejemplar.disponible = True

    def fuera_de_plazo(self, dia_actual):
        return (not self.devuelto) and dia_actual > self.dia_entrega
    

from prestamo import Prestamo


class Lector:
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.prestamos = []

    def tomar_prestado(self, ejemplar, dia_actual):
        if not ejemplar.disponible:
            print('El ejemplar no está disponible')
        
        prestamo = Prestamo(ejemplar, self.nombre, dia_actual)
        ejemplar.disponible = False
        self.prestamos.append(prestamo)
        return prestamo
    
    def devolver(self, ejemplar):
        for p in self.prestamos:
            if p.ejemplar == ejemplar and not p.devuelto:
                p.devolucion()
                return p
            else:
                print('Este lector no ha tomado este ejemplar prestado')
    
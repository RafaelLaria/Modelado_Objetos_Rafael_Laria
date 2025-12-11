class Ejemplar:
    def __init__(self, id_ejemplar):
        self.id_ejemplar = id_ejemplar
        self.disponible = True

    def __str__(self):
        if self.disponible:
            estado = 'Disponible'
        else:
            estado = 'Prestado'
        return f'Ejemplar{self.id_ejemplar}, {estado}'
    
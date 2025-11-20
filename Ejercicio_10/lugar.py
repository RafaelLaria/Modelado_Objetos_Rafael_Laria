class Lugar:
    def __init__(self):
        self.nombre2 = ""
        self.x = ""
        self.y = ""
    def __str__(self):
        return 'LUGAR DE ACTUACIÓN\n' \
        f'NOMBRE DEL LUGAR: {self.nombre2}\n' \
        f'COORDENADA X: {self.x}\n' \
        f'COORDENADA Y: {self.y}\n'
    def dar_nombre2(self):
        self.nombre2 = input('Nombre del lugar:')
    def dar_x(self):
        self.x = int(input('Coordenada X:'))
    def dar_y(self):
        self.y = int(input('Coordenada Y:'))
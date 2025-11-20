class Proyecto(Lugar):
    def __init__(self):
        super().__init__(self)
        self.nombre = ""
        self.fecha_inicio = ""
        self.fecha_fin = ""
    def __str__(self):
        return 'PROYECTO\n' \
               f'NOMBRE: {self.nombre}\n' \
               f'FECHA DE INICIO: {self.fecha_inicio}\n' \
               f'FECHA DE FINAL: {self.fecha_fin}\n'
    def dar_nombre(self):
        self.nombre = input('Nombre del proyecto:')
    def dar_fecha1(self):
        self.fecha_inicio = input('Fecha de inicio:')
    def dar_fecha2(self):
        self.fecha_fin = input('Fecha de final:')

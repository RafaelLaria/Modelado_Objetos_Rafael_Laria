class Actuacion:
    def __init__(self):
        self.fecha_inicio = ""
        self.fecha_fin = ""
        self.tipo = ""
    def __str__(self):
        return f'FECHA DE INICIO: {self.fecha_inicio}\n' \
               f'FECHA DE FINAL: {self.fecha_fin}\n' \
               f'TIPO: {self.tipo}'
    def dar_fecha1(self):
        self.fecha_inicio = input('Fecha de inicio:')
    def dar_fecha2(self):
        self.fecha_fin = input('Fecha de final:')
    def dar_tipo(self):
        print('Tipo de actuación:\n' \
              '1)Sondeo\n' \
              '2)Excavación\n' \
              '3)Seguimiento')
        tipo = int(input('Escoja un tipo de actuación:'))
        if tipo == 1:
            self.tipo = 'Sondeo'
        elif tipo == 2:
            self.tipo = 'Escavación'
        elif tipo == 3:
            self.tipo = 'Seguimiento'
        else:
            print('Escoja una de las tres opciones')
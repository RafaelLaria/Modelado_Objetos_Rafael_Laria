class Cuadro:
    def __init__(self, titulo, cronologia, autor):
        self.titulo = titulo
        self.cronologia = cronologia
        self.autor = autor
        self.tecnica = ""
        self.subtecnica = ""
        self.material = ""
        self.estado = ""
    def __str__(self):
        return f'TÍTULO: {self.titulo}\n' \
        f'CRONOLOGÍA: {self.cronologia}\n' \
        f'AUTOR: {self.autor}\n' \
        f'TÉCNICA: {self.tecnica}\n' \
        f'SUBTÉCNICA: {self.subtecnica}\n' \
        f'MATERIAL: {self.material}\n' \
        f'ESTADO DE CONSERVACIÓN: {self.estado}'
    def dar_tecnica(self):
        opcion_correcta1 = 2
        while True:
            print('1)Acuarela\n' \
                '2)Óleo\n' \
                '3)Pastel\n' \
                '4)Fresno')
            opcion = int(input('Escoja la tecnica:'))
            if opcion == opcion_correcta1:
                self.tecnica = 'Óleo'
                break
            else:
                print('Incorrecto, vuelva a escoger')
    def dar_subtecnica(self):
        opcion_correcta2 = 1
        while True:
            print('1)Sfumato\n' \
                '2)Pincelada simple\n' \
                '3)Collage\n' \
                '4)Veladura')
            opcion1 = int(input('Escriba la subtécnica: '))
            if opcion1 == opcion_correcta2:
                self.subtecnica = 'Sfumato'
                break
            else:
                print('Incorrecto, vuelva a escoger')
    def dar_material(self):
        opcion_correcta3 = 1
        while True:
            print('1)Madera de nogal y de olmo\n' \
                '2)Lienzo')
            opcion2 = int(input('Escoja el material: '))
            if opcion2 == opcion_correcta3:
                self.material = 'Madera de nogal y de olmo'
                break
            else:
                print('Incorrecto, vuelva a escoger')
    def dar_estado(self):
        opcion_correcta4 = 3
        while True:
            print('1)Excelente\n' \
                '2)Bueno\n' \
                '3)Regular\n' \
                '4)Malo\n' \
                '5)Destruido')
            opcion3 = int(input('Escoja el estado: '))
            if opcion3 == opcion_correcta4:
                self.estado = 'Regular'
                break
            else:
                print('Incorrecto, vuelva a escoger')
    
class Persona:
    def __init__(self):
        self.nombre = ""
        self.primer_apellido = ""
        self.segundo_apellido = ""
        self.fecha_nacimiento = ""
        self.sexo = ""
        self.numero_identificacion = ""
        self.padre = None
        self.madre = None
        self.hijos = []
        self.pareja = None
    def __str__(self):
        return f'NOMBRE: {self.nombre}\n' \
               f'APELLIDO 1: {self.primer_apellido}\n' \
               f'APELLIDO 2: {self.segundo_apellido}\n' \
               f'FECHA DE NACIMIENTO: {self.fecha_nacimiento}\n' \
               f'SEXO:{self.sexo}\n' \
               f'NUMERO DE IDENTIFICACION: {self.numero_identificacion}\n'
    
    def dar_nombre(self):
        self.nombre = input('Nombre:')
    def dar_apellido1(self):
        self.primer_apellido = input('Apellido1:')
    def dar_apellido2(self):
        self.segundo_apellido = input('Apellido2:')
    def dar_fecha(self):
        self.fecha_nacimiento = input('Fecha de nacimiento:')
    def dar_sexo(self):
        self.sexo = input('Dar sexo:')
    def dar_numero(self):
        self.numero_identificacion = input('Número de identificación:')
        if len(self.numero_identificacion) == 8 and self.numero_identificacion[:7].isdigit() and self.numero_identificacion[-1].isalpha():
            print(self.numero_identificacion)
        else:
            print('El numero de identificación debe tener 8 caracteres, el ultimo siendo una letra')


    def que_es(self, persona1, persona2):
        

        



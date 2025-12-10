class Estructura:
    def __init__(self, codigo, fecha):
        self.codigo = codigo
        self.fecha = fecha
        self.materiales = []
        self.sub_estructura = []
    
    def __str__(self):
        return f'Código: {self.codigo}\n' \
               f'Fecha: {self.fecha}\n' \
               f'Materiales: { self.materiales}'
    
    
    def dar_material(self):
        while len(self.materiales) < 5:
            material = input('Escriba el material de la estructura: ')
            self.materiales.append(material)

    def agregar_sub_estructura(self, estructura):
        if not isinstance(estructura, Estructura):
            raise ValueError('La subestructura debe ser una subestructuraa en sí')
        else:
            self.sub_estructura.append(estructura)
    
    def mostrar_subestructuras(self):
        print(f'Subestrucuturas de {self.codigo}')
        for i in self.sub_estructura:
            print(i.codigo)


if __name__ == '__main__':
    e1 = Estructura('123456789', '10/12/25')
    e1.dar_material()

    e2 = Estructura('987654321', '12/10/25')
    e2.dar_material()

    e1.agregar_sub_estructura(e2)
    e1.mostrar_subestructuras()

    print(e1)
    print(e2) 

    
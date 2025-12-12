class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.espacios = []

    def agregar_espacios(self, espacio):
        self.espacios.append(espacio)
    
class Espacio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []
        self.ciudad = None
    
    def agregar_edificios(self, edificio):
        self.edificios.append(edificio)

class Calle(Espacio):
    pass

class Plaza(Espacio):
    pass

class Edificio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ornamentos = []
        self.espacio = None
    
    def agregar_ornamentos(self, ornamento):
        self.ornamentos.append(ornamento)

class Ornamento:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.edificio = None

    def __str__(self):
        return f'{self.nombre}:{self.tipo}'
    

if __name__ == '__main__':
    ciudad = Ciudad('Cangas de Onis')
    calle = Calle('Avenida de Covadonga')
    plaza = Plaza('Plaza del ayuntamiento')
    ciudad.agregar_espacios(calle)
    ciudad.agregar_espacios(plaza)

    e = Edificio('Hotel Granda')
    fachada = Ornamento('Pared','Blanca')

    e.agregar_ornamentos(fachada)
    calle.agregar_edificios(e)


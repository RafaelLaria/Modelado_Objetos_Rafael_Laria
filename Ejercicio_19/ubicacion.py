class Ubicacion:
    def __init__(self, codigo):
        self.codigo = codigo

class Sala(Ubicacion):
    def __init__(self, codigo, nombre):
        super().__init__(codigo)
        self.nombre = nombre
        self.esta_abierto = True

    def accesible(self):
        return self.esta_abierto
    
class Almacen(Ubicacion, Sala):
    def __init__(self, codigo, nombre):
        super().__init__(codigo)
        self.nombre = nombre

    def accesible(self):
        return not self.esta_abierto

        
class Planta:
    def __init__(self, numero):
        self.numero = 0

class Edificio:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.plantas = []

    def agregar_plantas(self):
        cantidad = int(input('¿Cuantas plantas quieres que tenga el edificio?: '))
        for planta in range(cantidad+1):
            planta = Planta()
            self.plantas.append(planta)


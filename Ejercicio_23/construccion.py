class Construccion:
    def __init__(self, nombre):
        self.nombre = nombre

class Edificio(Construccion):
    
    def mostrar(self, nivel = 0):
        print(' ' * nivel + f' - Edificio : {self.nombre}')

class ConjuntoConstruido(Construccion):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.construcciones = []

    def agregar(self, construccion):
        self.construcciones.append(construccion)

    def eliminar(self, construccion):
        self.construcciones.remove(construccion)

    def mostrar(self, nivel = 0):
        print(' ' * nivel + f'+Conjunto: {self.nombre}')
        for c in self.construcciones:
            c.mostrar(nivel + 1)


if __name__ =='__main__':
    e1 = Edificio('1')
    e2 = Edificio('2')
    e3 = Edificio('3')

    c1 = ConjuntoConstruido('Plaza')
    c2 = ConjuntoConstruido('Calle')

    c1.agregar(e1)
    c1.agregar(e2)

    c2.agregar(c1)
    c2.agregar(e3)

    c2.mostrar()
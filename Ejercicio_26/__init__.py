class Ventana:
    def __init__(self, alto, ancho, arco, decoracion_exterior, tipo_cierre):
        self.alto = alto
        self.ancho = ancho
        self.arco = arco
        self.decoracion_exterior = decoracion_exterior
        self.tipo_cierre = tipo_cierre

    def __str__(self):
        return f"Ventana {self.alto}x{self.ancho}, arco {self.arco}, decoración: {self.decoracion_exterior}, cierre: {self.tipo_cierre}"


class Absides:
    def __init__(self, cantidad, forma, ventanas):
        self.cantidad = cantidad
        self.forma = forma
        self.ventanas = ventanas

    def __str__(self):
        return f"{self.cantidad} ábsides {self.forma} con {len(self.ventanas)} ventanas cada uno"


class Nave:
    def __init__(self, cantidad=1):
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.cantidad} nave(s)"


class Crucero:
    def __init__(self, brazos_salientes=False):
        self.brazos_salientes = brazos_salientes

    def __str__(self):
        return "Con crucero de brazos salientes" if self.brazos_salientes else "Sin crucero saliente"


class Iglesia:
    def __init__(self, nombre, tipo, naves, absides, crucero, orientacion="Este"):
        self.nombre = nombre
        self.tipo = tipo
        self.naves = naves
        self.absides = absides
        self.crucero = crucero 
        self.orientacion = orientacion

    def __str__(self):
        return (f"Iglesia '{self.nombre}' ({self.tipo}):\n"
                f"{self.naves}\n"
                f"{self.crucero}\n"
                f"{self.absides}\n"
                f"Orientación: {self.orientacion}")


if __name__=='__main__':
    ventanas_rural = [Ventana(alto=2, ancho=1, arco="doble", decoracion_exterior="sin decorar", tipo_cierre="tela encerada") for _ in range(2)]
    absides_rural = Absides(cantidad=1, forma="simple", ventanas=ventanas_rural)
    nave_rural = Nave(cantidad=1)
    crucero_rural = Crucero(brazos_salientes=False)
    iglesia_rural = Iglesia("San Pedro", "rural", naves=nave_rural, absides=absides_rural, crucero=crucero_rural)

    # Ventanas de iglesia mayor
    ventanas_mayor = [Ventana(alto=3, ancho=1, arco="doble", decoracion_exterior="decorada", tipo_cierre="vidriera incolora") for _ in range(3)]
    absides_mayor = Absides(cantidad=3, forma="semicircular", ventanas=ventanas_mayor)
    nave_mayor = Nave(cantidad=5)
    crucero_mayor = Crucero(brazos_salientes=True)
    iglesia_mayor = Iglesia("Santa María", "mayor importancia", naves=nave_mayor, absides=absides_mayor, crucero=crucero_mayor)

    print(iglesia_rural)
    print()
    print(iglesia_mayor)
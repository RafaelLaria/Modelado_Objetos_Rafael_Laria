class Hospital():
    def nombre(self):
        return "Hospital"

    def actividad(self):
        return "Atendiendo pacientes"


class Escuela():
    def nombre(self):
        return "Escuela"

    def actividad(self):
        return "Impartiendo clases"


class Vivienda():
    def nombre(self):
        return "Vivienda"

    def actividad(self):
        return "Albergando residentes"
    
class Edificio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estados = []

    def agregar_estado(self, estado):
        self.estados.append(estado)

    def quitar_estado(self, estado_tipo):
        self.estados = [e for e in self.estados if not isinstance(e, estado_tipo)]

    def mostrar_estados(self):
        if not self.estados:
            print(f"El edificio '{self.nombre}' no tiene estados activos.")
            return

        print(f"Estados activos del edificio '{self.nombre}':")
        for e in self.estados:
            print(f" - {e.nombre()}")

    def actividades(self):
        print(f"Actividades actuales en '{self.nombre}':")
        for e in self.estados:
            print(f" * ({e.nombre()}) {e.actividad()}")

if __name__=='__main__':
    ed = Edificio("Edificio Central")


    ed.agregar_estado(Escuela())
    ed.mostrar_estados()
    ed.actividades()

    print("\nAhora también es hospital:")
    ed.agregar_estado(Hospital())
    ed.mostrar_estados()
    ed.actividades()

    print("\nYa no es escuela:")
    ed.quitar_estado(Escuela)
    ed.mostrar_estados()
    ed.actividades()

    print("\nAhora también es vivienda:")
    ed.agregar_estado(Vivienda())
    ed.mostrar_estados()
    ed.actividades()
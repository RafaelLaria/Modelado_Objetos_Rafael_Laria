from enum import Enum

class TipoSitio(Enum):
    ASENTAMIENTO = "Asentamiento"
    ENTERRAMIENTO = "Enterramiento"
    AREA_EXPLOTACION = "Área de Explotación"
    CONJUNTO_ARQUEOLOGICO = "Conjunto Arqueológico"


class Tiempo:
    def __init__(self, inicio, fin=None):
        self.inicio = inicio
        self.fin = fin

    def __str__(self):
        if self.fin:
            return f"{self.inicio} - {self.fin}"
        return str(self.inicio)

class EntidadArqueologica:
    def __init__(self, nombre, tipo: TipoSitio, cronologia: Tiempo):
        self.nombre = nombre
        self.tipo = tipo
        self.cronologia = cronologia

    def __str__(self):
        return f"{self.nombre} ({self.tipo.value}), Cronología: {self.cronologia}"
    
class SitioArqueologico(EntidadArqueologica):
    def __init__(self, nombre, tipo: TipoSitio, cronologia: Tiempo, singular=True):
        super().__init__(nombre, tipo, cronologia)
        self.singular = singular

    def __str__(self):
        tipo_singular = "Singular" if self.singular else "Múltiple"
        return f"{super().__str__()} [{tipo_singular}]"

class Lugar:
    def __init__(self, nombre, provincia, dimensiones=None):
        self.nombre = nombre
        self.provincia = provincia
        self.dimensiones = dimensiones
        self.entidades = []

    def agregar_entidad(self, entidad: EntidadArqueologica):
        self.entidades.append(entidad)

    def __str__(self):
        info_entidades = "\n  ".join(str(e) for e in self.entidades)
        return f"Lugar: {self.nombre}, Provincia: {self.provincia}, Dimensiones: {self.dimensiones}\nEntidades Arqueológicas:\n  {info_entidades}"

if __name__=='__main__':
    cron1 = Tiempo(500, 1000)

    asentamiento = SitioArqueologico("Asentamiento de la Colina", TipoSitio.ASENTAMIENTO, cron1, singular=True)
    enterramiento = SitioArqueologico("Necrópolis Valle", TipoSitio.ENTERRAMIENTO, Tiempo(800, 1200), singular=False)

    lugar1 = Lugar("Valle Antiguo", "Provincia Ejemplo", dimensiones="100x200 m")
    lugar1.agregar_entidad(asentamiento)
    lugar1.agregar_entidad(enterramiento)

    print(lugar1)
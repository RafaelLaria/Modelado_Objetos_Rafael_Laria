from enum import Enum

class Tiempo:
    def __init__(self, inicio, fin=None):
        self.inicio = inicio
        self.fin = fin

    def __str__(self):
        return f"{self.inicio} - {self.fin}" if self.fin else str(self.inicio)

class Tecnica(Enum):
    PINTURA = "Pintura"
    ESCULTURA = "Escultura"
    DIBUJO = "Dibujo"

class SubTecnica(Enum):
    OLEO = "Óleo"
    ACUARELA = "Acuarela"
    BRONCE = "Bronce"

class Material(Enum):
    LIENZO = "Lienzo"
    MADERA = "Madera"
    PIEDRA = "Piedra"

class EstadoConservacion(Enum):
    EXCELENTE = "Excelente"
    BUENO = "Bueno"
    REGULAR = "Regular"
    MALO = "Malo"

class Lugar:
    def __init__(self, institucion, ciudad, pais):
        self.institucion = institucion
        self.ciudad = ciudad
        self.pais = pais

    def __str__(self):
        return f"{self.institucion}, {self.ciudad}, {self.pais}"

class Obra:
    def __init__(self, titulos, cronologia, tecnica, sub_tecnica, material_soporte, autor, estado_conservacion, lugar):
        self.titulos = titulos
        self.cronologia = cronologia
        self.tecnica = tecnica
        self.sub_tecnica = sub_tecnica
        self.material_soporte = material_soporte
        self.autor = autor
        self.estado_conservacion = estado_conservacion
        self.lugar = lugar
        self.replicas = []

    def agregar_replica(self, replica):
        self.replicas.append(replica)

    def __str__(self):
        titulos_str = ", ".join(self.titulos)
        replicas_str = ", ".join([r.titulos[0] for r in self.replicas]) if self.replicas else "Ninguna"
        return (f"Obra: {titulos_str}\nCronología: {self.cronologia}\nTécnica: {self.tecnica.value}, "
                f"Sub-técnica: {self.sub_tecnica.value}\nMaterial: {self.material_soporte.value}\n"
                f"Autor: {self.autor}\nEstado: {self.estado_conservacion.value}\nLugar: {self.lugar}\n"
                f"Réplicas: {replicas_str}")

if __name__ == '__main__':
    lugar1 = Lugar("Museo del Prado", "Madrid", "España")
    obra_original = Obra(["Las Meninas"], Tiempo(1656), Tecnica.PINTURA, SubTecnica.OLEO, Material.LIENZO, "Diego Velázquez", EstadoConservacion.EXCELENTE, lugar1)
    replica1 = Obra(["Las Meninas - Réplica"], Tiempo(1656), Tecnica.PINTURA, SubTecnica.OLEO, Material.LIENZO, "Artista Desconocido", EstadoConservacion.BUENO, lugar1)
    obra_original.agregar_replica(replica1)
    print(obra_original)
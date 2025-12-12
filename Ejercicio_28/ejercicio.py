class Tiempo:
    def __init__(self, inicio, fin=None):
        self.inicio = inicio
        self.fin = fin

    def __str__(self):
        return f"{self.inicio} - {self.fin}" if self.fin else str(self.inicio)

class ObjetoArqueologico:
    def __init__(self, codigo, datacion: Tiempo, dimensiones, descripcion, material):
        self.codigo = codigo
        self.datacion = datacion
        self.dimensiones = dimensiones
        self.descripcion = descripcion
        self.material = material
        self.similares = []

    def agregar_similar(self, otro_objeto):
        if otro_objeto not in self.similares:
            self.similares.append(otro_objeto)
            otro_objeto.similares.append(self)

    def __str__(self):
        return f"Objeto {self.codigo} ({self.material}), Dimensiones: {self.dimensiones}, Descripción: {self.descripcion}"

class ObjetoCompleto(ObjetoArqueologico):
    def __init__(self, codigo, datacion: Tiempo, dimensiones, descripcion, material, uso):
        super().__init__(codigo, datacion, dimensiones, descripcion, material)
        self.uso = uso
        self.componentes = []

    def agregar_componente(self, objeto):
        self.componentes.append(objeto)

    def __str__(self):
        componentes_str = ", ".join([c.codigo for c in self.componentes]) if self.componentes else "Ninguno"
        return (f"{super().__str__()}, Uso: {self.uso}, Componentes: {componentes_str}")

class Excavacion:
    def __init__(self, sitio):
        self.sitio = sitio
        self.objetos = []

    def agregar_objeto(self, objeto: ObjetoArqueologico):
        self.objetos.append(objeto)

    def __str__(self):
        objetos_str = "\n  ".join(str(o) for o in self.objetos)
        return f"Excavación en {self.sitio.nombre}:\n  {objetos_str}"

class SitioArqueologico:
    def __init__(self, nombre):
        self.nombre = nombre

if __name__=='__main__'

    sitio = SitioArqueologico("Colina Antigua")

    obj1 = ObjetoArqueologico("O001", Tiempo(500, 600), "10x5 cm", "Fragmento de cerámica pintada", "Cerámica")
    obj2 = ObjetoCompleto("O002", Tiempo(520, 580), "20x10 cm", "Vasija completa de almacenamiento", "Cerámica", "Almacenamiento de granos")
    obj2.agregar_componente(obj1)

    obj1.agregar_similar(obj2)

    excavacion = Excavacion(sitio)
    excavacion.agregar_objeto(obj1)
    excavacion.agregar_objeto(obj2)

    print(excavacion)
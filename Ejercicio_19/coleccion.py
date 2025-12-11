class Coleccion:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.objetos = []

    def agregar_objetos(self, objeto):
        self.objetos.append(objeto)
        return self.objetos
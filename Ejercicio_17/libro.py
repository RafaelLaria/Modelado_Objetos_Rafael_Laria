class Libro:
    def __init__(self, id_libro, titulo, autor, tematica):
        self.id = id_libro
        self.titulo = titulo
        self.autor = autor
        self.tematica = tematica
        self.ejemplares = []
    
    def __str__(self):
        return f'{self.titulo}({self.tematica})'
    
    def agregar_ejemplar(self, ejemplar):
        self.ejemplares.append(ejemplar)



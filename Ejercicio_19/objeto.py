class Objeto: 
    def __init__(self, codigo, nombre, autor, fecha_creacion, origen, tematica, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.autor = autor
        self.fecha_creacion = fecha_creacion
        self.origen = origen
        self.tematica = tematica
        self.estado = estado
    
    def __str__(self):
        return f'Codigo: {self.codigo}\n' \
               f'Nombre: {self.nombre}\n' \
               f'Autor: {self.autor}\n' \
               f'Fecha de creación: {self.fecha_creacion}\n' \
               f'Tematica: {self.tematica}\n' \
               f'Estado: {self.tematica}'
     


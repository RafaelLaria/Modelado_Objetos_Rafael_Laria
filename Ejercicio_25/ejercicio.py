class Hoja:
    def __init__(self, contenido):
        if contenido not in ('manuscrito','impreso'):
            raise ValueError('El contenido de una hoja debe ser manuscrito o impreso')
        self.material = 'papel'
        self.contenido = contenido

class Libro:
    def __init__(self, hojas, union):
        if not hojas:
            raise ValueError('Un libro debe tener al menos una hoja')
    
        for hoja in hojas:
            if hoja.material != 'papel':
                raise ValueError('Las hojas deben ser de papel')
            
        if union not in ('cosido','encuadernado'):
            raise ValueError('Un libro debe ser cosido o encuadernado')
        
        self.hojas = hojas
        self.union = union


class Muestra:
    def __init__(self, conjunto_original, porcion, metodo):
        if not conjunto_original:
            raise ValueError("Debe existir un conjunto original.")

        if not porcion:
            raise ValueError("La muestra debe ser una porción del conjunto.")

        
        self.conjunto_original = conjunto_original
        self.porcion = porcion
        self.metodo = metodo
class Tiempo:
    def __init__(self, inicio, fin=None):
        self.inicio = inicio
        self.fin = fin

    def __str__(self):
        return f"{self.inicio} - {self.fin}" if self.fin else str(self.inicio)

class Lugar:
    def __init__(self, nombre, provincia=None):
        self.nombre = nombre
        self.provincia = provincia

    def __str__(self):
        return self.nombre if not self.provincia else f"{self.nombre}, {self.provincia}"

class Ocupacion:
    def __init__(self, nombre, periodo: Tiempo):
        self.nombre = nombre
        self.periodo = periodo

    def __str__(self):
        return f"{self.nombre} ({self.periodo})"

class Lectura:
    def __init__(self, titulo, autor, periodo=None):
        self.titulo = titulo
        self.autor = autor
        self.periodo = periodo

    def __str__(self):
        return f"{self.titulo} por {self.autor}" + (f" ({self.periodo})" if self.periodo else "")

class Evento:
    def __init__(self, nombre, fecha: Tiempo):
        self.nombre = nombre
        self.fecha = fecha

    def __str__(self):
        return f"{self.nombre} ({self.fecha})"

class Persona:
    def __init__(self, nombre, apellidos, titulo=None, fecha_nacimiento=None, lugar_nacimiento=None,
                 fecha_fallecimiento=None, lugar_fallecimiento=None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.titulo = titulo
        self.fecha_nacimiento = fecha_nacimiento
        self.lugar_nacimiento = lugar_nacimiento
        self.fecha_fallecimiento = fecha_fallecimiento
        self.lugar_fallecimiento = lugar_fallecimiento

        
        self.ocupaciones = []       
        self.contactos = []         
        self.visitas = []          
        self.lecturas = []         
        self.eventos = []          

    def agregar_ocupacion(self, ocupacion: Ocupacion):
        self.ocupaciones.append(ocupacion)

    def agregar_contacto(self, persona):
        if persona not in self.contactos:
            self.contactos.append(persona)
            persona.contactos.append(self)

    def agregar_visita(self, lugar: Lugar, periodo: Tiempo):
        self.visitas.append((lugar, periodo))

    def agregar_lectura(self, lectura: Lectura):
        self.lecturas.append(lectura)

    def agregar_evento(self, evento: Evento):
        self.eventos.append(evento)

    def __str__(self):
        info = f"{self.nombre} {self.apellidos}"
        if self.titulo:
            info += f", Título: {self.titulo}"
        if self.fecha_nacimiento:
            info += f"\nNacimiento: {self.fecha_nacimiento} en {self.lugar_nacimiento}"
        if self.fecha_fallecimiento:
            info += f"\nFallecimiento: {self.fecha_fallecimiento} en {self.lugar_fallecimiento}"

        if self.ocupaciones:
            info += "\nOcupaciones:"
            for o in self.ocupaciones:
                info += f"\n  - {o}"

        if self.contactos:
            contactos_str = ", ".join([c.nombre + " " + c.apellidos for c in self.contactos])
            info += f"\nContactos: {contactos_str}"

        if self.visitas:
            visitas_str = ", ".join([f"{l.nombre} ({p})" for l, p in self.visitas])
            info += f"\nVisitas: {visitas_str}"

        if self.lecturas:
            lecturas_str = ", ".join([str(l) for l in self.lecturas])
            info += f"\nLecturas: {lecturas_str}"

        if self.eventos:
            eventos_str = ", ".join([str(e) for e in self.eventos])
            info += f"\nEventos: {eventos_str}"

        return info


if __name__ == '__main__':
    lugar_nacimiento = Lugar("Madrid")
    lugar_fallecimiento = Lugar("Barcelona")

    persona = Persona("Juan", "Pérez", titulo="Dr.", fecha_nacimiento="1970-01-01", lugar_nacimiento=lugar_nacimiento,
                    fecha_fallecimiento="2020-12-31", lugar_fallecimiento=lugar_fallecimiento)

    persona.agregar_ocupacion(Ocupacion("Profesor", Tiempo(1995, 2015)))
    persona.agregar_ocupacion(Ocupacion("Investigador", Tiempo(2016, 2020)))

    persona2 = Persona("Ana", "García")
    persona.agregar_contacto(persona2)

    persona.agregar_visita(Lugar("Museo del Prado"), Tiempo(2000, 2001))
    persona.agregar_lectura(Lectura("Historia de España", "Autor Desconocido", Tiempo(1998)))
    persona.agregar_evento(Evento("Conferencia sobre Historia", Tiempo("2010-05-20")))
class Tiempo:
    def __init__(self, inicio, fin=None):
        self.inicio = inicio
        self.fin = fin

    def __str__(self):
        return f"{self.inicio} - {self.fin}" if self.fin else str(self.inicio)

class Lugar:
    def __init__(self, nombre, coordenada_x, coordenada_y, alias=None):
        self.nombre = nombre
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.alias = alias or []

    def agregar_alias(self, nombre_alias):
        self.alias.append(nombre_alias)

    def __str__(self):
        alias_str = f" (Alias: {', '.join(self.alias)})" if self.alias else ""
        return f"{self.nombre}{alias_str} [{self.coordenada_x}, {self.coordenada_y}]"

class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lugares = [] 
        self.miembros = []

    def agregar_lugar(self, lugar: Lugar):
        self.lugares.append(lugar)

    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)

    def __str__(self):
        lugares_str = ", ".join(str(l) for l in self.lugares)
        miembros_str = ", ".join([m.persona.nombre for m in self.miembros])
        return f"Proyecto: {self.nombre}\nLugares: {lugares_str}\nMiembros: {miembros_str}"

class Persona:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.roles = []         
        self.proyectos = []    

    def agregar_rol(self, rol):
        self.roles.append(rol)

    def agregar_proyecto(self, proyecto):
        if proyecto not in self.proyectos:
            self.proyectos.append(proyecto)

    def __str__(self):
        roles_str = ", ".join(self.roles) if self.roles else "Sin roles"
        proyectos_str = ", ".join([p.nombre for p in self.proyectos]) if self.proyectos else "Sin proyectos"
        return f"{self.nombre} {self.apellidos} | Roles: {roles_str} | Proyectos: {proyectos_str}"

class Miembro:
    def __init__(self, persona: Persona, proyecto: Proyecto, fecha_inicio: Tiempo, fecha_fin=None):
        self.persona = persona
        self.proyecto = proyecto
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.lugares_actuacion = []
        
        persona.agregar_proyecto(proyecto)
        proyecto.agregar_miembro(self)

    def agregar_lugar_actuacion(self, lugar: Lugar):
        self.lugares_actuacion.append(lugar)

    def __str__(self):
        lugares_str = ", ".join([str(l) for l in self.lugares_actuacion]) if self.lugares_actuacion else "Sin lugares"
        fecha_fin_str = str(self.fecha_fin) if self.fecha_fin else "Actual"
        return f"{self.persona.nombre} en {self.proyecto.nombre} ({self.fecha_inicio} - {fecha_fin_str}), Lugares: {lugares_str}"


if __name__ == '__main__':

    lugar1 = Lugar("Excavación A", 40.4168, -3.7038)
    lugar2 = Lugar("Excavación B", 41.3851, 2.1734, alias=["Sitio B1", "Sitio B2"])


    proyecto1 = Proyecto("Proyecto Arqueológico 2025")
    proyecto1.agregar_lugar(lugar1)
    proyecto1.agregar_lugar(lugar2)

    persona1 = Persona("Juan", "Pérez")
    persona1.agregar_rol("Director")
    persona2 = Persona("Ana", "García")
    persona2.agregar_rol("Investigadora")

    miembro1 = Miembro(persona1, proyecto1, Tiempo("2025-01-01", "2025-12-31"))
    miembro1.agregar_lugar_actuacion(lugar1)

    miembro2 = Miembro(persona2, proyecto1, Tiempo("2025-02-01"))
    miembro2.agregar_lugar_actuacion(lugar2)

    print(proyecto1)
    print()
    print(miembro1)
    print(miembro2)
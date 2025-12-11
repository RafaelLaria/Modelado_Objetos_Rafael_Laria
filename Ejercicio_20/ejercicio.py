class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.roles = []

    def agregar_rol(self, rol):
        if rol not in self.roles:
            self.roles.append(rol)

class Rol:
    def __init__(self, persona):
        self.persona = persona
        persona.agregar_rol(self)

class Responsable(Rol):
    def __init__(self, persona):
        super().__init__(persona)
        self.proyectos_dirigidos = []

    def dirigir_proyecto(self, proyecto):
        self.proyectos_dirigidos.append(proyecto)
        proyecto.responsables.append(self) 

class Tecnico(Rol):
    def __init__(self, persona):
        super().__init__(persona)
        self.proyectos = []
        self.actuaciones = []

    def participar_en_proyecto(self, proyecto):
        self.proyectos.append(proyecto)
        proyecto.tecnicos.append(self)

    def participar_en_actuacion(self, actuacion):
        self.actuaciones.append(actuacion)
        actuacion.tecnicos.append(self)

class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.actuaciones = []
        self.responsables = []
        self.tecnicos = []

    def agregar_actuacion(self, actuacion):
        if actuacion not in self.actuaciones:
            self.actuaciones.append(actuacion)

    def __str__(self):
        return f'Proyecto: {self.nombre}\n' \
               f'Responsables: {self.responsables}\n' \
               f'Técnicos: {self.tecnicos}'
 
class Actuacion:
    def __init__(self, descripcion, proyecto):
        self.descripcion = descripcion
        self.proyecto = proyecto
        self.tecnicos = []
        proyecto.agregar_actuacion(self)

if __name__ == '__main__':
    p1 = Persona('Rafael')
    p2 = Persona('Pancho')
    p3 = Persona('Paco')

    r1 = Responsable(p1)
    r2 = Tecnico(p2)
    r3 = Tecnico(p3)

    p = Proyecto('Excavación')
    
    a1 = Actuacion(p, 'Excavar con una cuchara')
    a2 = Actuacion(p, 'Excavar con las manos')

    r1.dirigir_proyecto(p)
    r2.participar_en_proyecto(p)
    r2.participar_en_actuacion(a1)
    r3.participar_en_proyecto(p)
    r3.participar_en_actuacion(a2)

    print(p)
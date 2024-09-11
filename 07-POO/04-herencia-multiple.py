class Persona:
    def __init__(self,nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        return f'Hola mi nombre es {self.nombre}'
    

class Artista:
    def __init__(self, habilidad):
        self.habiliad = habilidad

    def mostrar_habilidad(self):
        return f'Esta es mi habilidad: {self.habiliad}'
    

# Clase que hereda varias clases y sus valores
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario,empresa): # Los valores para esta clase tambien se usaran en las demas
        Persona.__init__(self,nombre,edad, nacionalidad) # Envio nombre, edad, nacionalidad a la clase persona
        Artista.__init__(self, habilidad) # Envio habiliad a la clase artista
        self.salario = salario
        self.empresa = empresa

    def presentacion_empleado(self):
        return f'{ super().hablar() } y { super().mostrar_habilidad() }'


empleado = EmpleadoArtista( 'joffrey', 17, 'baratheon', 'mandar', '17100', 'kings landing' )
print( empleado.presentacion_empleado() )
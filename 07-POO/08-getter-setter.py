# Con los getter y setter podemos acceder a propiedades que sean privadas

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
    

persona = Persona('isaac', 25 )
print( persona.get_nombre() )
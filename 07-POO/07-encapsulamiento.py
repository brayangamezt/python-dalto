# Encapsulamiento en python equivale a los accesos public y private que se les da a los metodos y propiedades en otros lenguajes

class Persona:
    def __init__(self):
        self.__nombre = 'isaac' # con el doble guion bajo indicamos que es una propiedad privada
    
    def __saludo(self): # Con el doble guion bajo indicamos que es un metodo privado
        return 'Hola mundo, esto es un saludo'


persona = Persona()
print( persona.__nombre )
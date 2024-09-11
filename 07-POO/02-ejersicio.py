
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre 
        self.edad = edad
        self.grado = grado

    def Estudiar(self, lugar):
        return f'El estudiante {self.nombre} esta estudiando en {lugar}'
    

student = Estudiante( 'brayan', 29, '5' )

print( student.nombre )
print( student.edad )
print( student.grado )
print( student.Estudiar('su casa') )
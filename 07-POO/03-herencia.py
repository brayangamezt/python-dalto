
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad



class Empleado (Persona):
    def __init__(self,nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad) # indicamos las propiedades heredadas y evito poner self dentro de esta clase
        self.trabajo = trabajo
        self.salario = salario

    def Empleado_informacion(self):
        return f"El empleado {self.nombre}"


employee = Empleado( 'brayan', 29, 'mexicano', 'desarrollador', 10000 )
print( employee.nacionalidad )
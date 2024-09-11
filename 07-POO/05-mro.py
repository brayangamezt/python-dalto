# El MRo sirve para indicar que se va ejecutar en que orden en caso de que las clases repitan metodos o propiedades

class A:
    def hablar(self):
        print('hola desdes la A')

class B(A):
    def hablar(self):
        print('hola desde B')

class C(A):
    def hablar(self):
        print('hola desde C')

class D(B,C): # Despues da prioridad a la primera clase declarada y despues a la segunda
    def hablar(self): # La primera prioridad esta el metodo dentro de la misma clase
        print('hola desde D')


d = D()
print( d.hablar() )
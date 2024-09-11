celular1_marca = 'Samsung'
celular2_marca = 'Apple'
celular3_marca = 'Huawei'

celular1_modelo = 'S23'
celular2_modelo = 'Iphone 15'
celular3_modelo = 'P20 PRO'

celular1_camara = '48MP'
celular2_carama = '50MP'
celular3_camara = '48MP'

# Anteriormente estamos definiendo solamente 3 propiedades para 3 celulares
# Tuvimos que utilizar 9 lineas de codigo para esto por o que no es viable hacerlo
# Para evitar esto podemos utilizar las POO que sirven para ahorra y mantener codigo utilizando tambien clases



class Celular:
    def __init__(self, marca, modelo, camara): # Contructor de la clase
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

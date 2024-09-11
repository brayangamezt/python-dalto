# Un decorador en Python es esencialmente una función que toma otra función como argumento, y retorna una nueva función que envuelve (o reemplaza) la función original.
def decoradora(funcion):
    def nueva_funcion():
        print( 'antes de la funcion' )
        funcion()
        print('despues de la funcion')

    return nueva_funcion

# Estoy pasando la funcion saludo como parametro de la funcion decoradora
@decoradora
def saludo():
    print( 'hola mundo' )

# saludo tendra un retorno nuevo ya que decoramos su valor
# saludo()




# EJERSICIO EJEMPLO
def cache_filter(numero):
    numbers = []

    #Se toman todos los argumentos de la funcion original y se pasan a esta
    def number_saved(*args, **kwargs):
        print( args )
        print( numero )
        print( kwargs )
        pass
    
    return number_saved

# La funcion number_added sera argumento de la funcion cache_filter
@cache_filter
def number_added( number ):
    return f'+52{number}'

number_added('6624763758','6624492905')

# Cuando colocamos W como segundo porametro, es para sobreescribir lo que tenemos, y si el archivo no existe lo crea
with open('python_files.txt', 'w', encoding='UTF-8') as archivo:
    print('Escribiendo en el archivo')
    archivo.write('Veamos el funcionamiento' + '\n')

# Cuando colocamos A como segundo parametro, es para agregar informacion al archivo y si el archivo no existe lo crea
with open('python_files2.txt', 'a', encoding='UTF-8') as file:
    print('Agregando informacion: ')
    file.write('Hola mi nombre es Delcia Maria' + '\n')

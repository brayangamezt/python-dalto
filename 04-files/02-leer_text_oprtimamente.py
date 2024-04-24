with open('python_files.txt') as archivo:  # De esta forma abro el archivo y lo guardo en una variable archivo
    print('Hola, se logro abrir el archivo correctamente')  # Este print se va ejecutar si se logra abrir correctamente
    print(archivo.read())

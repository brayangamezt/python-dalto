# Para abrir un archivo TXT
file = open('python_files.txt', encoding='UTF-8')

# Si quiero leer el archivo y que me muestre todo su contenido se hace de la siguiente manera
print(file.read())

# Para leer una linea en especifico de nuestro archivo, se hace de la siguiente manera
lines = file.readlines()
print(lines)

file.write(f'Escribiendo mas informacion \n ')

# Cerrar el archivo
file.close()

# Un archivo CSV es un archivo que puede estar seperado por comas o columnas, es decir arhivos excel
import csv  # Esto nos sirve para trabajar con archivos CSV

with open('personas.csv') as people:

    file = csv.reader(people)  # Esta es otra forma de leer csv
    print(file)  # Esto nos arrojara un dato como este <_csv.reader object at 0x00000278FAFECC40>
    for data in file:  # Lo que debemos hacer es recorrerlo para que muestra su informacion
        print(data)

# Para recorrer dos listas al mismo tiempo en python se hace lo siguiente
names = ['Brayan', 'Isaac', 'Saul', 'Cristobal']
last_names = ['Gamez', 'Trujillo', 'Gonzales', 'Torres']

# Primera opcion para recorrer dos listas al mismo tiempo
for name, last_name in zip(names, last_names):
    print(f'El nombre compuesto es: {name} - {last_name}')

# Forma de recorrer una lista
for name in range(len(names)):
    print(names[name])

# Otra opcion para recorrer una lista, esta opcion me devuelve una tupla
for nam in enumerate(last_names):
    print(f'Valor completo de la tupla: {nam}')
    print(f'Primer valor de la tupla: {nam[1]}')

# ************************* ITERAR DICCIONARIOS ***********************

print('-------------------------- imprimiendo diccionarios ------------------')
persons = {
    'nombre': 'Brayan',
    'apellido': 'Gamez',
    'edad': 28,
    'nacionalidad': 'Mexicana'
}

# Esta es una forma de acceder a los valores del diccionario
for person in persons:
    print(persons[person])

# Otra forma de acceder a los diccionarios y que devuelva como resultado una tubla, es lo siguiente (nombre, brayan)
for person in persons.items():
    print(person)

#Devuelve los valores del diccionario persons --output: Brayan, Gamez, 28, Mexicana
for value in persons.values():
    print(value)

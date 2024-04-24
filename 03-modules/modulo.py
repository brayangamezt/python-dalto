import sys

# This is going to give us a tuple with all the python modules
print(sys.builtin_module_names)

# This is going to tell us where modules are
print(sys.path)

# If i want to add a module in another path to my current module i do next
new_path = 'C:\\Users\\BrayanGamez\\PycharmProjects\\CDalto\\02-functions'
sys.path.append(new_path)
print(sys.path)

import pruebas
print(pruebas.great_greet('Brayan'))

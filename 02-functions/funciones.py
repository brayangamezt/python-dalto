from functools import reduce

numbers = [10, 4, 11, 6, 9]
number_boolean = 12.5874

# Funcion para obtener el numero mayor de un iterable
max_number = max(numbers)
print(f'1.- Hightes number: {max_number}')

# Function to get the lowest number
min_number = min(numbers)
print(f'2.- Lower number: {min_number}')

# Function to return a number with specific numbers of decimals
number_round = round(number_boolean, 2)
print(f'3.- It round {number_round} with just two decimals')

# Boolean function to return a boolean function
bool_result = bool(0)
print(f'4.- Return a boolean value: {bool_result}')

# Return TRUE if whole the elements inside of an iterable element are true
all_results = all([10, 'sdfs', [False, 0], 'brayan'])
print(f'5.- The value of the iterable: {all_results}')

# Sum all the values in an iterable element
result = sum(numbers)
print(f'6.- Return the sum of the numbers element: {result}')


# -------------------------- UTILIZANDO EL PARAMETRO ARGS ----------------------


def names(*args):
    value = ''
    for name in args:
        print(f'These are the args {name}')
        value += f'{name}' + '\n'
    return value


names_for_args = ['brayan', 'Isaac', 'Alma', 'Vanessa']
print(names(names_for_args))


def ages(*args):
    for age in args:
        print(age)


ages(25, 45, 78, 15)

# ------------------------ LAMBDA FUNCTION -----------------
mul_per_two = lambda value: value * 2
print(mul_per_two(5))

# We can pass lambda function as expresion or condtion for another function as we show below
names = ['Brayan', 'isaac', 'Saul']
last_names = ['Gamez', 'Cordova', 'Beltran']

# In this case lambda function is a function that we are going to pase for each element of iterable elements
new_composer_names = map(lambda a, b: f'{a} {b}', names, last_names)
print(list(new_composer_names))

# Filter in python is to return new array with specific condition
ages = [5, 12, 17, 18, 24, 32]
major = filter(lambda x: x >= 18, ages)
print(list(major))


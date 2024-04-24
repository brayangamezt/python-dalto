import re  # modulo para trabajar con expresiones regulares

text = 'Hola maestro, esta es la linea 1. como esta mi capitan. Esta es la linea de texto 7 and next one 25'

# SEARCH: is looking for the first coinciden and return them
result = re.search('linea', text)
print(result)

# FindAll the coincidence and return them in one array. With ignorecase we transform to lowercase all
finding_all = re.findall('esta', text, flags=re.IGNORECASE)
print(finding_all)

# \d --> seek digits from 0-9
# \D --> return everything that is not a number
digits = re.findall(r"\d", text)
print(digits)

# \w to seek alphanumeric characters --> [a-z] [A-Z] and the '_'
# \W we get all what is not a character
alphanumeric = re.findall(r'\w', text)
print(alphanumeric)

# \s --> seek for white space, tabs,

# . --> seek for all the line break
# \ --> cancel special characters, using this befor characters, we are looking for a specific character

# making a chain with a number with a point and one space
looking_coincidence = re.findall(r'\d\.\s', text)
print(looking_coincidence)

# ^ --> Seek at the beggining of the text for a coincidence
start = re.findall(r'^hola', text, flags=re.IGNORECASE)
print(start)

# $ --> Looking for a coincidence at the end of text

# {} GROUPS --> looking for a group of specific value, for example two numbers together
numbers_joined = re.findall(r'\d{2}', text)
print(numbers_joined)

# {n,m} GROUP RANGE --> return coincidence of a range
new_groups = re.findall(r'\d{1,3}', text)
print(new_groups)

# SUB : Para remplazar valores de una expresion regular
sentence_one = 'The assure was obteined by maria'
sentence_two = re.sub(r'[aeiou]', '', sentence_one)
print(sentence_two)